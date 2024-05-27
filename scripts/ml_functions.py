"""
This script contains the implementation code for the machine-learning models
"""

from utils import *
from Shapley_Taylor_index import *
import os
import shap
import subprocess
import time
from sklearn.model_selection import GridSearchCV
from sklearn import svm as sk_svm
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.utils import resample
from sklearn.base import BaseEstimator, ClassifierMixin
from xgboost import XGBClassifier


# Hyperparameter space for the support vector machines
svm_cspace = 2. ** np.linspace(-5., 10., 10)
svm_gammaspace = 2. ** np.linspace(-10., 3., 10)


class PredictionModel:

    """ This class is used to train all models, compute the Shapley values, and 
        summarise the output in a dictionary
    """
    def __init__(self, model, name, data, config, **kwargs):
        """
         :param object model: Prediction model object in the standard sklearn format.
         :param str name: name given to the model.
         :param dict data: contains the training and test data
         :param Config config: config object. 
        """
        self.trainx = data["trainx"]
        self.trainy = data["trainy"]
        self.testx = data["testx"]
        self.config = config
        self.model = model
        self.name = name
        start_time = time.time()
        self._train() # train model 
        stop_time = time.time()

        self.best_hyper = None
        if hasattr(self.model, "best_params_"):
            self.best_hyper = model.best_params_
        if hasattr(self.model, "best_estimator_"):
            self.model = self.model.best_estimator_
        
        self.shapV, self.shapV_inter = self._compute_shap() # compute Shapley values

        self.output = {
            "name": name,
            "pred": model.predict_proba(self.testx)[:, 1],
            "fit": model.predict_proba(self.trainx)[:, 1],
            "model": self.model,
            "hyper_params": self.best_hyper,
            "shapley": self.shapV,
            "shapley_interaction": self.shapV_inter,
            "time": stop_time - start_time
        }

    def _train(self, **kwargs): # train the prediction model and obtain preditions
        self.model.fit(self.trainx, self.trainy, **kwargs)
    
    def _compute_shap(self): # compute Shapley values
        shapV_inter = None # Shapley values of the interaction of variables
        shapV = None # Shapley values of the individual variables

        if self.config.exp_do_shapley:
        
            if self.name in ["extree", "forest", "xgboost"]: # TreeExplainer
                explainerTree = shap.TreeExplainer(self.model)
                shapV = explainerTree.shap_values(self.testx)[1]
            
                if self.config.exp_shapley_interaction: # compute Shapley interaction
                    shapV_inter = explainerTree.shap_interaction_values(self.testx)[1]
                
            elif self.name in ["logreg"]:
                shap_linear = shap.LinearExplainer(self.model,
                                            masker = self.trainx)
                shapV = shap_linear.shap_values(self.testx)

            else: # KernelExplainer
                shapV = shapley_kernel_wrapper(self.model, self.trainx,
                                               self.testx, self.config)
   
    
        if self.config.exp_shapley_interaction:
            feature_names = self.config.feature_names_processed
            trainx_pd = pd.DataFrame(self.trainx, columns = feature_names)
            testx_pd = pd.DataFrame(self.testx, columns = feature_names)

            shapV_inter = Shapley_taylor_wrapper(self.model,trainx_pd, testx_pd,
                                k = self.config.exp_taylor_k,
                                features_select = self.config.exp_taylor_feature_select,
                                background_size = self.config.exp_shap_background,
                                probabilities = not self.name in ["logreg"],
                                sample_coalitions = self.config.exp_taylor_samples)
        return (shapV, shapV_inter)

def gaussianprocess(data, config, name, **kwargs):
    
    model = GaussianProcessClassifier()
    model_instance = PredictionModel(model, name, data, config, **kwargs)
    return model_instance.output


def logreg(data, config, sample_weight, name, **kwargs):
    # Logistic regression
    
    model = LogisticRegression(penalty="none", solver = "lbfgs")
    model_instance = PredictionModel(model, name, data, config,
                                     sample_weight = sample_weight)
    return model_instance.output



def extree(data, config, sample_weight, cv_hyper, do_cv, name, **kwargs):
    # Extremely randomised trees.
    # We use the default parameters (do_cv = False) in the paper, as hyperparameter tuning does not imporve the performance
    
    if do_cv:
        hyperparameters = {'max_features': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           'max_depth': [2, 3, 4, 5, 7, 10, 12, 15, 20]
                           }
        model = hyperparam_search(ExtraTreesClassifier(n_estimators=1000,  n_jobs=1),
                                    hyperparameters,
                                    use=config.exp_search,
                                    n_jobs=config.exp_n_kernels, cv=cv_hyper,
                                    scoring=config.exp_optimization_metric,
                                    n_iter=config.exp_n_iter_rsearch,
                                    verbose=config.exp_verbose)
    else:
        
        model = ExtraTreesClassifier(n_estimators=1000, n_jobs=config.exp_n_kernels)

    model_instance = PredictionModel(model, name, data, config,
                                     sample_weight = sample_weight)
    return model_instance.output

def forest(data, config, sample_weight, cv_hyper, do_cv, name, **kwargs):
    # Random forest.
    # We use the default parameters (do_cv = False) in the paper, as hyperparameter tuning does not imporve the performance

    if do_cv:
       
        hyperparameters = {'max_features': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           'max_depth': [2, 3, 4, 5, 7, 10, 12, 15, 20]
                           }
        model = hyperparam_search(RandomForestClassifier(n_estimators=1000,  n_jobs=1),
                                    hyperparameters,
                                    use=config.exp_search,
                                    n_jobs=config.exp_n_kernels, 
                                    cv=cv_hyper,
                                    scoring=config.exp_optimization_metric,
                                    n_iter=config.exp_n_iter_rsearch,
                                    verbose=config.exp_verbose)

    else:
        
        model = RandomForestClassifier(n_estimators=1000, n_jobs=config.exp_n_kernels)

    model_instance = PredictionModel(model, name, data, config, sample_weight = sample_weight)
    return model_instance.output



#code for a decision tree
def decision_tree(data, config, sample_weight, cv_hyper, do_cv, name, **kwargs):
    # Decision tree.
    # We use the default parameters (do_cv = False) in the paper, as hyperparameter tuning does not improve the performance

    if do_cv:
       
        hyperparameters = {'max_features': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           'max_depth': [2, 3, 4, 5, 7, 10, 12, 15, 20]
                           }
        model = hyperparam_search(DecisionTreeClassifier(),  # Using DecisionTreeClassifier
                                    hyperparameters,
                                    use=config.exp_search,
                                    n_jobs=config.exp_n_kernels, 
                                    cv=cv_hyper,
                                    scoring=config.exp_optimization_metric,
                                    n_iter=config.exp_n_iter_rsearch,
                                    verbose=config.exp_verbose)

    else:
        
        model = DecisionTreeClassifier()  # Using DecisionTreeClassifier

    model_instance = PredictionModel(model, name, data, config, sample_weight=sample_weight)
    return model_instance.output


#CODE for xgboost
def xgboost(data, config, sample_weight, cv_hyper, do_cv, name, **kwargs):
    # see https://xgboost.readthedocs.io/en/latest/python/python_api.html   
    xgb = XGBClassifier(objective='binary:logistic', eval_metric = "auc", nthread=-1, n_estimators=500)
    model = GridSearchCV(
        xgb,
        {"max_depth": [2, 4, 6],
        "n_estimators": [50, 100, 250],
        'learning_rate': [0.01, 0.05, .2, .8],
        'subsample': [.7,.9, 1],
        'colsample_bytree': [.6,.9, 1]},
        verbose=1,
        n_jobs=-1,
        )

    model_instance = PredictionModel(model, name, data, config, sample_weight = sample_weight)
    return model_instance.output

#code for KNN
def knn(data, config, sample_weight, cv_hyper, do_cv, name, **kwargs):
    knn = KNeighborsClassifier()
    parameters = {
        'n_neighbors': [3,4, 5,6, 7,8,9,10],
        'weights': ['uniform', 'distance'],
        'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
        'leaf_size': [30, 50, 100],
        'p': [1, 2]
    }

    model = GridSearchCV(knn, parameters, cv=cv_hyper, verbose=1, n_jobs=-1)

    model_instance = PredictionModel(model, name, data, config, sample_weight=sample_weight)
    return model_instance.output


def nnet_single(data, cv_hyper, config, name, **kwargs):
    # Single neural network
    
    n_features = data["trainx"].shape[1]
    hyperparameters = {'alpha': 10.0 ** np.linspace(-3.0, 3.0, 10),
                       'hidden_layer_sizes': list(
                               set([round(n_features / 3.0), round(n_features / 2.0), n_features,
                                    (n_features, n_features),
                                    (n_features, round(n_features / 2.0)),
                                    (n_features*2, n_features), 
                                    (n_features*2, n_features*2)
                                    ])),
                        'activation': ['tanh',"relu","logistic"]}
    
    # Exclude single neuron or zero neuron network
    hyperparameters["hidden_layer_sizes"] = list(set(hyperparameters["hidden_layer_sizes"]).difference(set([0, (1, 0)])))
    
    model = hyperparam_search(MLPClassifier(solver='lbfgs', max_iter=1000),
                               hyperparameters,
                               use=config.exp_search,
                               n_jobs=config.exp_n_kernels, cv=cv_hyper,
                               scoring=config.exp_optimization_metric,
                               n_iter=10000,
                               verbose=config.exp_verbose)
    model_instance = PredictionModel(model, name, data, config)
    return model_instance.output


def nnet_multi(data, config, group, name,  **kwargs):
    # Neural network ensemble
    ''' Fitting this ensemble is very slow and only recommended on a high performance cluster. The ensemble #
    searchers for hyperparameters for each of the 25 base model in the ensemble to increase the variance
     across models '''
    
    resample="bootstrap" # resample is one of the following ["bootstrap", "copy", "upsample"], 
    n_features = data["trainx"].shape[1]
    hyperparameters = {'alpha': 10.0 ** np.linspace(-3.0, 3.0, 10),
                       'hidden_layer_sizes': list(
                               set([round(n_features / 3.0), round(n_features / 2.0), n_features,
                                    (n_features, n_features),
                                    (n_features, round(n_features / 2.0)),
                                    (n_features*2, n_features), 
                                    (n_features*2, n_features*2)
                                    ])),
                        'activation': ['tanh', 'relu']}
    
    # Exclude single neuron or zero neuron network
    hyperparameters["hidden_layer_sizes"] = list(set(hyperparameters["hidden_layer_sizes"]).difference(set([0, (1, 0)])))
    
    model = NnetMultiObj(resample=resample, config=config,
                     hyperparameters=hyperparameters, group=group)
    model_instance = PredictionModel(model, name, data, config)
    return model_instance.output
    
class NnetMultiObj(BaseEstimator, ClassifierMixin):
    # Train neural networks in the neural network ensemble  
    
    start = time.time()

    def __init__(self, resample, config, hyperparameters, group):
        self.models = list()
        self.n_models = 25
        self.resample = resample
        self.hyperparameters = hyperparameters
        self.config = config
        self.group = group

    def fit(self, X, y=None):
        for _ in np.arange(self.n_models):

            if self.resample == "bootstrap":
                x_rs, y_rs, group_rs = resample(X, y, self.group, replace=True)
            elif self.resample == "upsample":
                x_rs, y_rs, group_rs = upsample(X, y,
                                                group=self.group,
                                                costs={0: y.mean(), 1: 1 - y.mean()})
            else: x_rs, y_rs, group_rs = X, y, self.group

            cv_hyper, cv_fold_vector = create_grouped_folds(y_rs, group_rs, nfolds=5, reps=1)

            m = hyperparam_search(MLPClassifier(solver='lbfgs', max_iter=1000),
                                  self.hyperparameters,
                                  use=self.config.exp_search,
                                  n_jobs=self.config.exp_n_kernels, cv=cv_hyper,
                                  scoring=self.config.exp_optimization_metric,
                                  n_iter=self.config.exp_n_iter_rsearch,
                                  verbose=self.config.exp_verbose)
            m.fit(x_rs, y_rs)
            self.models.append(m)
        return self

    def predict_proba(self, X, y=None):
        predm = np.zeros((X.shape[0], self.n_models, 2)) * np.nan
        for m in np.arange(len(self.models)):
            predm[:, m, :] = self.models[m].predict_proba(X)
        return predm.mean(axis=1)


def svm_single(data, cv_hyper, config, sample_weight, name, **kwargs):
    # Support-vector machine with radial basis function kernel
    
    hyperparameters= {'C': svm_cspace, 'gamma': svm_gammaspace}
    model = hyperparam_search(sk_svm.SVC(kernel='rbf', probability=True),
                          hyperparameters,
                          use=config.exp_search,
                          n_jobs=config.exp_n_kernels,
                          cv=cv_hyper,
                          scoring=config.exp_optimization_metric,
                          n_iter=config.exp_n_iter_rsearch,
                          verbose=config.exp_verbose)
    model_instance = PredictionModel(model, name, data, config,
                                     sample_weight = sample_weight)
    return model_instance.output



def svm_multi(data, config, group, sample_weight, name, **kwargs):
    # Support vector machine ensemble ensemble
    ''' Fitting this ensemble is very slow and only recommended on a high performance cluster. The ensemble #
    searchers for hyperparameters for each of the 25 base model in the ensemble to increase the variance
     across models '''
      

    resample = "upsample" # resample is one of the following ["none", "bootstrap", "copy", "upsample"]

    if config.exp_do_upsample and (resample=="upsample"):
       raise ValueError("The SVM ensemble upsamples the data already, It is not recommended to upsample another time \
           using the the exp_do_upsample of the Config class.")
       
    hyperparameters = {'C': svm_cspace, "gamma": svm_gammaspace}
    model = SvmMultiObj(config=config, hyperparameters=hyperparameters,
                        group=group, resample=resample,
                       sample_weight=sample_weight)
    
    model_instance = PredictionModel(model, name, data, config)
    return model_instance.output
  
class SvmMultiObj(BaseEstimator, ClassifierMixin):
       # Train support vector machines in the support vector machine ensemble  
    start = time.time()
    def __init__(self, config, hyperparameters, group, resample, sample_weight):
        self.models = list()
        self.n_models = 25 # number of models in the ensemble
        self.hyperparameters = hyperparameters
        self.config = config
        self.group = group
        self.resample = resample
        self.sample_weight = sample_weight

    def fit(self, X, y=None):
        for _ in np.arange(self.n_models):

            if self.resample == "bootstrap":
                x_rs, y_rs, group_rs = resample(X, y, self.group, replace=True)
            elif self.resample == "upsample":
                x_rs, y_rs, group_rs = upsample(X, y, 
                                                group=self.group,
                                                costs={0: y.mean(), 1: 1 - y.mean()})
            else: x_rs, y_rs, group_rs = X, y, self.group


            cv_hyper, cv_fold_vector = create_grouped_folds(y_rs, group_rs, nfolds=5, reps=1)

            m = hyperparam_search(sk_svm.SVC(kernel='rbf', probability=True),
                              self.hyperparameters,
                              use=self.config.exp_search,
                              n_jobs=self.config.exp_n_kernels, cv=cv_hyper,
                              scoring=self.config.exp_optimization_metric,
                              n_iter=self.config.exp_n_iter_rsearch,
                              verbose=self.config.exp_verbose)
            if self.resample == "upsample":
                m.fit(x_rs, y_rs)
            else:
                m.fit(x_rs, y_rs, sample_weight=self.sample_weight)

            self.models.append(m)
        return self

    def predict_proba(self, X, y=None):
        predm = np.zeros((X.shape[0], self.n_models, 2)) * np.nan
        for m in np.arange(len(self.models)):
            predm[:, m, :] = self.models[m].predict_proba(X)
        return predm.mean(axis=1)


