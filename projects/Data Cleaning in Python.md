**In this practice, we performed some data cleaning tasks:**
1) Checking for completeness
2) Renaming variables for easy referencing
3) Changing data types
4) Visualise continuous variables through boxplot
5) Filtering outliers.
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The dataset Mall_Customers.csv can be found here:
url = "https://raw.githubusercontent.com/Nicholasglim/general-projects/main/datasets/Mall_Customers.csv"
data = pd.read_csv(url)

# Checking whether rows/columns tally with info on kaggle
data.shape
```
(200, 5)
```
# Previewing first 5 rows of dataset
data.head()
```
| CustomerID | Gender | Age | Annual.Income..k.. | Spending.Score..1.100. |
|----------- |------- |---- |------------------- |----------------------- |
| 1          | Male   | 19  | 15                 | 39                     |
| 2          | Male   | 21  | 15                 | 81                     |
| 3          | Female | 20  | 16                 | 6                      |
| 4          | Female | 23  | 16                 | 77                     |
| 5          | Female | 31  | 17                 | 40                     |
```
# Summary statistics for each variable
data.describe()
```
|       |   CustomerID   |       Age      |  Annual.Income..k.. | Spending.Score..1.100. |
|-------|--------------- |--------------- |-------------------- |----------------------- |
| count | 200.000000     | 200.000000     | 200.000000          | 200.000000             |
| mean  | 100.500000     | 38.850000      | 60.560000           | 50.2000000             |
| std   | 57.879185      | 13.969007      | 26.234721           | 25.823522              |
| min   | 1.000000       | 18.000000      | 15.000000           | 1.000000               |
| 25%   | 50.750000      | 28.750000      | 41.500000           | 34.750000              |
| 50%   | 100.500000     | 36.000000      | 61.500000           | 50.000000              |
| 75%   | 150.250000     | 49.000000      | 78.000000           | 73.000000              |
| max   | 200.00         | 70.000000      | 137.000000          | 99.000000              |
```
# Checking for missing values
data.isnull().sum()
```
| CustomerID | Gender | Age | Annual.Income..k.. | Spending.Score..1.100. |
|------------|--------|-----|--------------------|------------------------|
| 0          | 0      | 0   | 0                  | 0                      |
```
# Checking for duplicate values
data.duplicated().sum()
```
0
```
# Renaming column names for easy referencing
data.rename(columns={
    'CustomerID': 'customer_id',
    'Gender': 'gender',
    'Age': 'age',
    'Annual Income (k$)': 'annual_income_k$',
    'Spending Score (1-100)': 'spending_score'
    }, inplace=True)

# Verifying changes
data.columns
```
'customer_id', 'gender', 'age', 'annual_income_k$', 'spending_score'
```
# Checking data types
data.dtypes
```
|CustomerID | Gender | Age   | Annual Income (k$) | Spending Score (1-100) |
|-----------|--------|-------|--------------------|------------------------|
| int64     | object | int64 | int64              | int64                  |
```
# Converting dtype (object) to (category)
data['gender'] = data['gender'].astype('category')

# Verifying changes
data['gender'].dtype
```
CategoricalDtype(categories=['Female', 'Male'], ordered=False, categories_dtype=object)
```
# Visualise distributions using boxplots. Detected outlier in 'annual_income_k$'
numeric_columns = ['age', 'annual_income_k$', 'spending_score']
for col in numeric_columns:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=data[col])
        plt.title(f'Boxplot of {col}')
        plt.show()
```
"Age" Boxplot                                                                        | "Annual Income" Boxplot                                                              | "Spending Score" Boxplot
:-----------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------
![](https://github.com/user-attachments/assets/f5f493a7-e77e-4713-acdc-277034c99fa9) | ![](https://github.com/user-attachments/assets/1637b7eb-f9ae-4374-9255-826bbe90e01b) | ![](https://github.com/user-attachments/assets/244ebf1f-93cf-4344-8454-3f9f73d54e6c)
```
# Handling outlier in 'annual_income_k$' using IQR method
Q1 = data['annual_income_k$'].quantile(0.25)
Q3 = data['annual_income_k$'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identifying outliers
outliers = data[(data['annual_income_k$'] < lower_bound) | (data['annual_income_k$'] > upper_bound)]

print(outliers)
```
| customer_id | gender | age   | annual_income_k$ | spending_score |
|-------------|--------|-------|------------------|----------------|
| 199         | Male   | 32    | 137              | 18             |
| 200         | Male   | 30    | 137              | 83             |
```
# Filtering out outlier in 'annual_income_k$'
data_filtered = data[(data['annual_income_k$'] >= lower_bound) & (data['annual_income_k$'] <= upper_bound)]

print(data_filtered)
```
[198 rows x 5 columns]
