library(tidyr)
library(dplyr)
df <- read.csv('/Users/Joey/Desktop/2020_experiment/replication_material/data/JSTR6myvars.csv')
df2 <- readxl::read_xlsx("/Users/Joey/Downloads/global_crisis_data.xlsx") 
countries <- c("Sweden", "Portugal","Norway","Netherlands", "Japan","Italy","UK"
               ,"France", "Finland","Spain", "Denmark","Germany","Switzerland","Canada","Belgium",
               "Australia", "USA","Ireland","United States", "United Kingdom") #make a list of countries from the paper
years <- seq(1871,2020)
df <- filter(df, country %in% countries)
df2 <- filter(df2, Country %in% countries)
df <- filter(df, year %in% years)
df2 <- filter(df2, Year %in% years)
View(df)

#do the same for RR crises, see how our definitions of crisis match up.
df_JST = subset(df, select = c('year',"country","iso",'crisisCurrency',"crisisInflation","crisisJST"))
df_RR = subset(df2, select = c('Year',"Country","Currency Crises", "Inflation Crises","Banking Crisis"))
df_RR <- df_RR %>% rename(country = 'Country') #Rename a column
df_RR <- df_RR %>% rename(year = 'Year')
View(df_JST)

df_combined <- merge(df_JST,df_RR) 
View(df_combined)
df_combined$`Currency Crises`[df_combined$`Currency Crises` == '2'] <- 1
df_combined$crisisCurrency[df_combined$crisisCurrency == '#DIV/0!'] <- 0
df_combined$crisisInflation[df_combined$crisisInflation == '#DIV/0!'] <- 0
table(df_yay$crisisCurrency)
table(df_yay$crisisInflation)
table(df_yay$`Inflation Crises`)
table(df_yay$`Currency Crises`)
table(df_combined$`Banking Crisis`)
table(df_combined$crisisJST)

#this checks where our def matches the RR definitions for currency crises
matching_positive_cases <- which(df_combined$crisisCurrency == df_combined$`Currency Crises` & df_combined$crisisCurrency == 1)

# Subset the data frame to show only matching positive cases
matching_positive_df <- df_combined[matching_positive_cases, ]

# Show the resulting subset
View(matching_positive_df)
#only 4 years where they agree! wow! check for similar years?

#this checks where our def matches the RR definitions for inflation crises
matching_positive_cases <- which(df_combined$crisisInflation == df_combined$`Inflation Crises` & df_combined$crisisInflation == 1)

# Subset the data frame to show only matching positive cases
matching_positive_df <- df_combined[matching_positive_cases, ]

# Show the resulting subset
View(matching_positive_df)
#59 years of matching (out of about 80 is pretty good)

#this checks where our def matches the RR definitions for banking crises
matching_positive_cases <- which(df_combined$crisisJST == df_combined$`Banking Crisis` & df_combined$crisisJST == 1)

# Subset the data frame to show only matching positive cases
matching_positive_df <- df_combined[matching_positive_cases, ]

# Show the resulting subset
View(matching_positive_df)
#56 out of 76 agreement.


# Create a dataframe with all combinations of countries and years from 2017 to 2020
new_years_df <- expand.grid(country = unique(df_RR$country), year = 2017:2020)

# Add a column with zeros for the observations
new_years_df$`Banking Crisis` <- 0
new_years_df$`Banking Crisis`<- as.character(new_years_df$`Banking Crisis`)

# Bind the new dataframe to the original dataframe
df_R <- bind_rows(df_RR, new_years_df)
View(df_R)
#rename US and UK
df_R$country[df_R$country == 'United States'] <- "USA"
df_R$country[df_R$country == 'United Kingdom'] <- "UK"

df_yay <- merge(df_R, df_JST)
df_yay$`Currency Crises`[df_yay$`Currency Crises` == '2'] <- 1
df_yay$crisisCurrency[df_yay$crisisCurrency == '#DIV/0!'] <- 0
df_yay$crisisInflation[df_yay$crisisInflation == '#DIV/0!'] <- 0
#rename variables for consistency
df_yay <- df_yay %>% rename(crisisBanking = 'Banking Crisis')

df_yay$crisisBanking[df_yay$crisisBanking == 'n/a'] <- NA



#Change the crisis variables from character to categorical
df_yay$crisisBanking <- as.factor(df_yay$crisisBanking)
df_yay$crisisInflation <- as.factor(df_yay$crisisInflation)
df_yay$crisisCurrency <- as.factor(df_yay$crisisCurrency)
df_yay$crisisJST <- as.factor(df_yay$crisisJST)

## got the data frame, so now its time to just decide if to put any 1s anywhere.
write.csv(df_yay, file = "../data/updated_crises_definitions.csv")
