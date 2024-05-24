# We  execute this script before doing  other analyses.
# It loads the raw data creates the pre-processed data
library(dplyr)

crises <- read.csv("../data/updated_crises_definitions.csv")
#df_raw <- readxl::read_excel("../data/JSTdatasetR3.xlsx", sheet = "Data")
df_raw <- read.csv('/Users/Joey/Desktop/2020_experiment/replication_material/data/JSTR6myvars.csv')
df_raw$crisisCurrency <- as.numeric(df_raw$crisisCurrency)
df_raw$crisisInflation <- as.numeric(df_raw$crisisInflation)
df_raw$crisis <- df_raw$crisisInflation
df_raw$crisisInflation <- NULL



#### process data ####

df <- df_raw

df$tdbtserv <- df$tloans * df$ltrate / 100

df <- df %>% group_by(country) %>% mutate(
  drate = ltrate - stir,
  tloan_gdp_rdiff3 = tloans / gdp  - lagit(tloans / gdp, lag = 3),
  tloan_gdp_rdiff2 = tloans / gdp  - lagit(tloans / gdp, lag = 2),
  bmon_gdp_rdiff2 = money/gdp - lagit(money/gdp, lag = 2),
  pdebt_gdp_rdiff2 = debtgdp - lagit(debtgdp, lag = 2),
  inv_gdp_rdiff2 = iy - lagit(iy, lag = 2),
  ca_gdp_rdiff2 = ca/gdp - lagit(ca/gdp, lag = 2),
  tdbtserv_gdp_rdiff2 = tdbtserv/gdp - lagit(tdbtserv/gdp, lag = 2),
  
  cpi_pdiff2 = perc_change(cpi, lag = 2),
  wage_pdiff2 = perc_change(wage, lag = 2),
  unemp_pdiff2 = perc_change(unemp, lag = 2),
  cons_pdiff2 = perc_change(rconsbarro, lag = 2),
  hp_pdiff2 = perc_change(hpnom, lag = 2),
  
  hloan_gdp_rdiff2 = thh / gdp  - lagit(thh / gdp, lag = 2),
  bloan_gdp_rdiff2 = tbus / gdp  - lagit(tbus / gdp, lag = 2)
  
)                     

df$srate <- df$stir
df$lrate <- df$ltrate
df <- df %>% group_by(country) %>% 
  mutate(cpi_pdiff1 = perc_change(cpi, lag = 1) * 100)




df <- df %>% group_by(year) %>% mutate(
  global_loan  = mean_no_self(tloan_gdp_rdiff2),
  global_drate = mean_no_self(drate))

df <- df %>% group_by(country) %>% mutate(crisis_lead1 = leadit(crisis, lag = 1),
                                          crisis_lead2 = leadit(crisis, lag = 2),
                                          crisis_lead3 = leadit(crisis, lag = 3),
                                          crisis_lead4 = leadit(crisis, lag = 4),
                                          
                                          crisis_lag1 = lagit(crisis, lag = 1),
                                          crisis_lag2 = lagit(crisis, lag = 2),
                                          crisis_lag3 = lagit(crisis, lag = 3),
                                          crisis_lag4 = lagit(crisis, lag = 4)
)
df_processed <- df

rm(df)
