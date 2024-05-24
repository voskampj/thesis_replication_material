#### produces Shapley regression (Table VI) ####

source("utils_analysis.R")
source("global.R")

algo <- "extree"
folder_experiment <- "baseline/"
result_files <- list.files(paste0("../results_raw/", folder_experiment))

df_shap <- read.csv(paste0("../results_raw/", folder_experiment, "shapley_append_", algo, ".txt"), sep ="\t")[,-1]
df <- read.csv(paste0("../results_raw/", folder_experiment, "data.txt"), sep ="\t")[,-1]


n_obs <- nrow(df)
n_rep <- nrow(df_shap) / n_obs
iter <- rep(1:n_rep, each = n_obs)



f_names <- setdiff(colnames(df_shap), c("crisis", "iso", "pred", "year", "index"))

# based on this analysis defined a function
tab <- shapley_regression(data = df_shap, iter, y_name = "crisis", features = f_names, avg_fun = mean)
tab <- tab[-1,] # remove intercept
tab$shapley_share <- colMeans(abs(df_shap[,f_names]))
tab$shapley_share <- tab$shapley_share / sum(tab$shapley_share)


# get the "direction" from a logistic regression on the actual features (not Shapely values)
tab$direction <- sign(glm(df[, c("crisis", f_names)], family = binomial(link='logit'))$coefficients[-1])
