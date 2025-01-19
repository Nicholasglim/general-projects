
library(dplyr)
library(tidyr)

url <- "https://raw.githubusercontent.com/Nicholasglim/general-projects/refs/heads/main/datasets/Mall_Customers.csv"
data <- read.csv(url)

```
# Checking whether rows/columns tally with info on kaggle 
dim(data)
```
# Previewing first 5 rows of dataset
head(data)

# Summary statistics for each variable
summary(data)

# Checking for missing values
colSums(is.na(data))

# Checking for duplicate
sum(duplicated(data))

# Renaming column names for easy referencing
colnames(data) <- c("customer_id", "gender", "age", "annual_income_k$", "spending_score")

# Verifying changes
colnames(data)

# Checking structure of data
str(data)

# Converting "Gender" for Factor
data$gender <- as.factor(data$gender)

# Verifying changes 
class(data$gender)

# Visualise distributions using boxplots. Detected outlier in 'annual_income_k$'
boxplot(data$age, main = "age")
boxplot(data$'annual_income_k$', main = "Annual Income")
boxplot(data$spending_score, main = "Spending Score")

# Handling outlier in 'annual_income_k$' using IQR method
Q1 <- quantile(data$`annual_income_k$`, 0.25)
Q3 <- quantile(data$`annual_income_k$`, 0.75)
IQR <- Q3 - Q1
lower_bound <- Q1 - 1.5 * IQR
upper_bound <- Q3 + 1.5 * IQR

# Identifying outliers
outliers <- data %>%
  filter(`annual_income_k$` < lower_bound | `annual_income_k$` > upper_bound)

print(outliers)

# Filtering out outliers
data_filtered <- data %>% 
  filter(`annual_income_k$` >= lower_bound & `annual_income_k$` <= upper_bound)

# Verifying changes
dim(data_filtered)
