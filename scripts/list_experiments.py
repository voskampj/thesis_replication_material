experiments = {


               
    100: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff","wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    200: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    300: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    400: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    #The following use a different crisis variable, based on RR dataset rather than thresholds
    3900: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"CurrencyRR",
        "description": "CurrencyRR, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    4900: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"InflationRR",
        "description": "InflationRR, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },

#baseline experiments to run just extree many many times to obtain very stable results                   
    10: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },

    20: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    30: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    40: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },

     44: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals, no nominal wages",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },

                

                       # House prices added, used for robustness checks
    1001: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals and house prices",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    2001: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals and house prices",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    3001: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals and house prices",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    4001: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals and house prices",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
      
                   
    1002: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals and house prices",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_gdp_rdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    2002: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals and house prices",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_gdp_rdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    3002: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals and house prices, wage_gdp_rdiff",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_gdp_rdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    4002: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals and house prices",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", "wage_gdp_rdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
  
    
       #classify the actual crisis year, not 1 and 2 years before            
    1100: {
        "crisis_indicators": False,
        "data_include_crisis_year": True,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals",
        "data_post_crisis": 0,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    2100: {
        "crisis_indicators": False,
        "data_include_crisis_year": True,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals",
        "data_post_crisis": 0,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    3100: {
        "crisis_indicators": False,
        "data_include_crisis_year": True,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals",
        "data_post_crisis": 0,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    4100: {
        "crisis_indicators": False,
        "data_include_crisis_year": True,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals",
        "data_post_crisis": 0,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
   
### robustness check experiments! JST

    101: {
        "description": "HP filter on GDP ratios",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_hp", "wage_pdiff","unemp_pdiff", "cons_pdiff" ,
                                     "pdebt_gdp_hp", "inv_gdp_hp", "ca_gdp_hp", "tloan_gdp_hp",
                                     "tdbtserv_gdp_hp", "global_tloan_gdp_hp", "global_drate"]

    },
    102: {
            "description": "HP filter on nominal variables",
            "crisis_indicators": True,
            "data_include_crisis_year": False,
            "crisis_definition":"JST",
            "data_post_crisis": 4,
            "data_feature_names":  ["drate", "global_drate", 
                                        "cpi_pdiff", "unemp_pdiff","wage_pdiff", "cons_pdiff",
                                        "tdbtserv_gdp_hp",
                                        "log_bmon_hp_norm", "log_pdebt_hp_norm", "log_inv_hp_norm", "log_tloan_hp_norm", 
                                        "ca_gdp_hp", 
                                        "global_log_tloan_hp_norm", "log_gdp_hp_norm"]
    },
    103: {
            "description": "HP filter on nominal variables",
            "crisis_indicators": True,
            "data_include_crisis_year": False,
            "crisis_definition":"JST",
            "data_post_crisis": 4,
            "data_feature_names":  ["drate", "global_drate", 
                                        "cpi_pdiff", "wage_pdiff","unemp_pdiff", "cons_pdiff",
                                        "tdbtserv_gdp_hp",
                                        "log_bmon_real_hp_norm", "log_pdebt_real_hp_norm", "log_inv_real_hp_norm", "log_tloan_real_hp_norm", 
                                        "ca_gdp_hp",
                                        "global_log_tloan_real_hp_norm", "log_gdp_real_hp_norm"]
    },

    104: {
        "description": "Hamilton filter on GDP ratios",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_ham", "wage_pdiff","unemp_pdiff", "cons_pdiff",
                                     "pdebt_gdp_ham", "inv_gdp_ham", "ca_gdp_ham", "tloan_gdp_ham",
                                     "tdbtserv_gdp_ham", "global_tloan_gdp_ham", "global_drate"]

    },

    105: {
        "description": "Replace slope of the yield curve with nominal short and long rate",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "data_post_crisis": 4,
         "data_feature_names": ["srate", "lrate", "cpi_pdiff", "bmon_gdp_rdiff", "wage_pdiff","unemp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]


    },
    106: {
        "description": "Replace slope of the yield curve with real short and long rate",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "data_post_crisis": 4,
        "data_feature_names": ["srate_real", "lrate_real", "cpi_pdiff", "bmon_gdp_rdiff", "wage_pdiff","unemp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
    },

### robustness check experiments! Banking

    201: {
        "description": "HP filter on GDP ratios",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_hp", "wage_pdiff","unemp_pdiff", "cons_pdiff" ,
                                     "pdebt_gdp_hp", "inv_gdp_hp", "ca_gdp_hp", "tloan_gdp_hp",
                                     "tdbtserv_gdp_hp", "global_tloan_gdp_hp", "global_drate"]

    },
    202: {
            "description": "HP filter on nominal variables",
            "crisis_indicators": True,
            "data_include_crisis_year": False,
            "crisis_definition":"Banking",
            "data_post_crisis": 4,
            "data_feature_names":  ["drate", "global_drate", 
                                        "cpi_pdiff", "unemp_pdiff","wage_pdiff", "cons_pdiff",
                                        "tdbtserv_gdp_hp", 
                                        "log_bmon_hp_norm", "log_pdebt_hp_norm", "log_inv_hp_norm", "log_tloan_hp_norm", 
                                        "ca_gdp_hp",
                                        "global_log_tloan_hp_norm", "log_gdp_hp_norm"]
    },
    203: {
            "description": "HP filter on nominal variables",
            "crisis_indicators": True,
            "data_include_crisis_year": False,
            "crisis_definition":"Banking",
            "data_post_crisis": 4,
            "data_feature_names":  ["drate", "global_drate", 
                                        "cpi_pdiff", "wage_pdiff","unemp_pdiff", "cons_pdiff",
                                        "tdbtserv_gdp_hp", 
                                        "log_bmon_real_hp_norm", "log_pdebt_real_hp_norm", "log_inv_real_hp_norm", "log_tloan_real_hp_norm", 
                                        "ca_gdp_hp", 
                                        "global_log_tloan_real_hp_norm", "log_gdp_real_hp_norm"]
    },

    204: {
        "description": "Hamilton filter on GDP ratios",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_ham", "wage_pdiff","unemp_pdiff", "cons_pdiff",
                                     "pdebt_gdp_ham", "inv_gdp_ham", "ca_gdp_ham", "tloan_gdp_ham",
                                     "tdbtserv_gdp_ham", "global_tloan_gdp_ham", "global_drate"]

    },

    205: {
        "description": "Replace slope of the yield curve with nominal short and long rate",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "data_post_crisis": 4,
         "data_feature_names": ["srate", "lrate", "cpi_pdiff", "bmon_gdp_rdiff", "wage_pdiff","unemp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]


    },
    206: {
        "description": "Replace slope of the yield curve with real short and long rate",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "data_post_crisis": 4,
        "data_feature_names": ["srate_real", "lrate_real", "cpi_pdiff", "bmon_gdp_rdiff", "wage_pdiff","unemp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
    },

### robustness check experiments! Currency

    301: {
        "description": "HP filter on GDP ratios",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_hp", "wage_pdiff","unemp_pdiff", "cons_pdiff" ,
                                     "pdebt_gdp_hp", "inv_gdp_hp", "ca_gdp_hp", "tloan_gdp_hp",
                                     "tdbtserv_gdp_hp", "global_tloan_gdp_hp", "global_drate"]

    },
    302: {
            "description": "HP filter on nominal variables",
            "crisis_indicators": True,
            "data_include_crisis_year": False,
            "crisis_definition":"Currency",
            "data_post_crisis": 4,
            "data_feature_names":  ["drate", "global_drate", 
                                        "cpi_pdiff", "unemp_pdiff","wage_pdiff", "cons_pdiff",
                                        "tdbtserv_gdp_hp", 
                                        "log_bmon_hp_norm", "log_pdebt_hp_norm", "log_inv_hp_norm", "log_tloan_hp_norm", 
                                        "ca_gdp_hp", 
                                        "global_log_tloan_hp_norm", "log_gdp_hp_norm"]
    },
    303: {
            "description": "HP filter on nominal variables",
            "crisis_indicators": True,
            "data_include_crisis_year": False,
            "crisis_definition":"Currency",
            "data_post_crisis": 4,
            "data_feature_names":  ["drate", "global_drate", 
                                        "cpi_pdiff", "wage_pdiff","unemp_pdiff", "cons_pdiff",
                                        "tdbtserv_gdp_hp", 
                                        "log_bmon_real_hp_norm", "log_pdebt_real_hp_norm", "log_inv_real_hp_norm", "log_tloan_real_hp_norm", 
                                        "ca_gdp_hp", 
                                        "global_log_tloan_real_hp_norm", "log_gdp_real_hp_norm"]
    },

    304: {
        "description": "Hamilton filter on GDP ratios",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_ham", "wage_pdiff","unemp_pdiff", "cons_pdiff",
                                     "pdebt_gdp_ham", "inv_gdp_ham", "ca_gdp_ham", "tloan_gdp_ham",
                                     "tdbtserv_gdp_ham", "global_tloan_gdp_ham", "global_drate"]

    },

    305: {
        "description": "Replace slope of the yield curve with nominal short and long rate",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "data_post_crisis": 4,
         "data_feature_names": ["srate", "lrate", "cpi_pdiff", "bmon_gdp_rdiff", "wage_pdiff","unemp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]


    },
    306: {
        "description": "Replace slope of the yield curve with real short and long rate",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "data_post_crisis": 4,
        "data_feature_names": ["srate_real", "lrate_real", "cpi_pdiff", "bmon_gdp_rdiff", "wage_pdiff","unemp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
    },

    ### robustness check experiments! Inflation

    401: {
        "description": "HP filter on GDP ratios",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_hp", "wage_pdiff","unemp_pdiff", "cons_pdiff" ,
                                     "pdebt_gdp_hp", "inv_gdp_hp", "ca_gdp_hp", "tloan_gdp_hp",
                                     "tdbtserv_gdp_hp", "global_tloan_gdp_hp", "global_drate"]

    },
    402: {
            "description": "HP filter on nominal variables",
            "crisis_indicators": True,
            "data_include_crisis_year": False,
            "crisis_definition":"Inflation",
            "data_post_crisis": 4,
            "data_feature_names":  ["drate", "global_drate", 
                                        "unemp_pdiff","wage_pdiff", "cons_pdiff",
                                        "tdbtserv_gdp_hp", 
                                        "log_bmon_hp_norm", "log_pdebt_hp_norm", "log_inv_hp_norm", "log_tloan_hp_norm", 
                                        "ca_gdp_hp", 
                                        "global_log_tloan_hp_norm", "log_gdp_hp_norm"]
    },
    403: {
            "description": "HP filter on nominal variables",
            "crisis_indicators": True,
            "data_include_crisis_year": False,
            "crisis_definition":"Inflation",
            "data_post_crisis": 4,
            "data_feature_names":  ["drate", "global_drate", 
                                         "wage_pdiff","unemp_pdiff", "cons_pdiff",
                                        "tdbtserv_gdp_hp",
                                        "log_bmon_real_hp_norm", "log_pdebt_real_hp_norm", "log_inv_real_hp_norm", "log_tloan_real_hp_norm", 
                                        "ca_gdp_hp", 
                                        "global_log_tloan_real_hp_norm", "log_gdp_real_hp_norm"]
    },

    404: {
        "description": "Hamilton filter on GDP ratios",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_ham", "wage_pdiff","unemp_pdiff", "cons_pdiff",
                                     "pdebt_gdp_ham", "inv_gdp_ham", "ca_gdp_ham", "tloan_gdp_ham",
                                     "tdbtserv_gdp_ham", "global_tloan_gdp_ham", "global_drate"]

    },

    405: {
        "description": "Replace slope of the yield curve with nominal short and long rate",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "data_post_crisis": 4,
         "data_feature_names": ["srate", "lrate", "bmon_gdp_rdiff", "wage_pdiff","unemp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]


    },
    406: {
        "description": "Replace slope of the yield curve with real short and long rate",
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "data_post_crisis": 4,
        "data_feature_names": ["srate_real", "lrate_real", "bmon_gdp_rdiff", "wage_pdiff","unemp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
    },

# Train models just after WW2 to see if we can obtain a better model

    
               
    1500: {
        "crisis_indicators": True,
        "data_period": 'post-ww2',
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    2500: {
        "crisis_indicators": True,
        "data_period": 'post-ww2',
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    3500: {
        "crisis_indicators": True,
        "data_period": 'post-ww2',
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    4500: {
        "crisis_indicators": True,
        "data_period": 'post-ww2',
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", #"bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    #Because of shortnened period, add house prices
    1510: {
        "crisis_indicators": True,
        "data_period": 'post-ww2',
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    2510: {
        "crisis_indicators": True,
        "data_period": 'post-ww2',
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    3510: {
        "crisis_indicators": True,
        "data_period": 'post-ww2',
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    4510: {
        "crisis_indicators": True,
        "data_period": 'post-ww2',
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "hp_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
        #Train the models using only the statistically significant predictors determined by Shapley regressions
    1: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "data_period": 'all',
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, only stat sig variables",
        "data_post_crisis": 4,
        "data_feature_names": ["cpi_pdiff","drate", "unemp_pdiff", "wage_pdiff",
                               "hp_pdiff", "cons_pdiff",
                               "pdebt_gdp_rdiff", "ca_gdp_rdiff",
                               "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff",
                               "global_loan", "global_drate"]
        
        },
    2: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Currency, indicators, 4 removed, only stat sig variables",
        "data_post_crisis": 4,
        "data_feature_names": ["cpi_pdiff","drate", "wage_pdiff",
                               "hp_pdiff", "cons_pdiff",
                               "pdebt_gdp_rdiff", "ca_gdp_rdiff",
                               "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff",
                               "global_loan", "global_drate","bmon_gdp_rdiff"]
        
        },
    3: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, only stat sig variables",
        "data_post_crisis": 4,
        "data_feature_names": ["cpi_pdiff","drate",
                               "hp_pdiff", "cons_pdiff",
                               "pdebt_gdp_rdiff",
                                "tdbtserv_gdp_rdiff",
                               "global_loan", "global_drate"]
        
        },
    4: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Currency, indicators, 4 removed, only stat sig variables",
        "data_post_crisis": 4,
            "data_feature_names": [ "global_drate", "wage_pdiff","cons_pdiff",
                                   "drate"]
        
        },
    #The next experiments use corporate debt, mentioned in appendix

    109: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    209: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    309: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    409: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", "unemp_pdiff", "wage_pdiff", "bdebt_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    ##No unemployment
        108: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "wage_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    208: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "wage_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    308: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff", "wage_pdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    408: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff",  "wage_pdiff", 
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    
    
    ### No wages, combine 107-109 into a table w baseline
   107: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"JST",
        "description": "JST, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    207: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Banking",
        "description": "Banking, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
                
    307: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Currency",
        "description": "Currency, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "cpi_pdiff", "bmon_gdp_rdiff",
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    407: {
        "crisis_indicators": True,
        "data_include_crisis_year": False,
        "crisis_definition":"Inflation",
        "description": "Inflation, indicators, 4 removed, with globals",
        "data_post_crisis": 4,
        "data_feature_names": ["drate", "bmon_gdp_rdiff", 
                                     "cons_pdiff", "pdebt_gdp_rdiff", "inv_gdp_rdiff", "ca_gdp_rdiff",
                                     "tloan_gdp_rdiff", "tdbtserv_gdp_rdiff", "global_loan", "global_drate"]
        
        },
    
}


