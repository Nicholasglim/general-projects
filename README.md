**In this practice, we performed some data cleaning tasks:**
1) Checking for completeness
2) Renaming variables for easy referencing
3) Changing data types
4) Visualise continuous variables through boxplot
5) Filtering outliers.
```
library(dplyr)
library(tidyr)

url <- "https://raw.githubusercontent.com/Nicholasglim/general-projects/refs/heads/main/datasets/Mall_Customers.csv"
data <- read.csv(url)

# Checking whether rows/columns tally with info on kaggle 
dim(data)
```
200   5
```
# Previewing first 6 rows of dataset
head(data)
```
| CustomerID | Gender | Age | Annual.Income..k.. | Spending.Score..1.100. |
|----------- |------- |---- |------------------- |----------------------- |
| 1          | Male   | 19  | 15                 | 39                     |
| 2          | Male   | 21  | 15                 | 81                     |
| 3          | Female | 20  | 16                 | 6                      |
| 4          | Female | 23  | 16                 | 77                     |
| 5          | Female | 31  | 17                 | 40                     |
| 6          | Female | 22  | 17                 | 76                     |

```
# Summary statistics for each variable
summary(data)
```
|   CustomerID   |     Gender        |       Age      |  Annual.Income..k.. | Spending.Score..1.100. |
|--------------- |------------------ |--------------- |-------------------- |----------------------- |
| Min.   :  1.00 |  Length:200       |  Min.   :18.00 |  Min.   : 15.00     | Min.   : 1.00          |
| 1st Qu.: 50.75 |  Class :character |  1st Qu.:28.75 |  1st Qu.: 41.50     | 1st Qu.:34.75          |
| Median :100.50 |  Mode  :character |  Median :36.00 |  Median : 61.50     | Median :50.00          |
| Mean   :100.50 |                   |  Mean   :38.85 |  Mean   : 60.56     | Mean   :50.20          |
| 3rd Qu.:150.25 |                   |  3rd Qu.:49.00 |  3rd Qu.: 78.00     | 3rd Qu.:73.00          |
| Max.   :200.00 |                   |  Max.   :70.00 |  Max.   :137.00     | Max.   :99.00          |
```
# Checking for missing values
colSums(is.na(data))
```
| CustomerID | Gender | Age | Annual.Income..k.. | Spending.Score..1.100. |
|----------- |------- |---- |------------------- |----------------------- |
| 0          | 0      | 0   | 0                  | 0                      |  
```
# Checking for duplicate
sum(duplicated(data))
```
0
```
# Renaming column names for easy referencing
colnames(data) <- c("customer_id", "gender", "age", "annual_income_k$", "spending_score")

# Verifying changes
colnames(data)
```
"customer_id"      "gender"           "age"              "annual_income_k$" "spending_score"  
```
# Checking structure of data
str(data)
```
|'data.frame':	      | 200 obs. of  5 variables:                |
|-------------------- |----------------------------------------- |
| $ customer_id     : | int  1 2 3 4 5 6 7 8 9 10 ...            |
| $ gender          : | chr  "Male" "Male" "Female" "Female" ... |
| $ age             : | int  19 21 20 23 31 22 35 23 64 30 ...   |
| $ annual_income_k$: | int  15 15 16 16 17 17 18 18 19 19 ...   |
| $ spending_score  : | int  39 81 6 77 40 76 6 94 3 72 ...      |
```
# Converting "Gender" for Factor
data$gender <- as.factor(data$gender)

# Verifying changes 
class(data$gender)
```
"factor"
```
# Visualise distributions using boxplots. Detected outlier in 'annual_income_k$'
boxplot(data$age, main = "age")
boxplot(data$'annual_income_k$', main = "Annual Income")
boxplot(data$spending_score, main = "Spending Score")
```
"Age" Boxplot                                                                        | "Annual Income" Boxplot                                                                       | "Spending Score" Boxplot
:-----------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------:
![](https://github.com/user-attachments/assets/b8464b15-3ec3-4155-b2cc-26133ee27fb7) | ![" Boxplot](https://github.com/user-attachments/assets/f72caf44-83c0-4d47-b9ba-df0623ac0706) | !["Spending Score" Boxplot](https://github.com/user-attachments/assets/3a937caf-c484-4794-b7a8-889f72bd78a6)
```
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
```
Outliers
| customer_id | gender | age | annual_income_k$ | spending_score |
|------------ |------- |---- |----------------- |--------------- |
| 199         |Male    | 32  | 137              | 18             | 
| 200         |Male    | 30  | 137              | 83             |
```
# Filtering out outliers
data_filtered <- data %>% 
  filter(`annual_income_k$` >= lower_bound & `annual_income_k$` <= upper_bound)

# Verifying changes
dim(data_filtered)
```
198   5
