```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
# The dataset Mall_Customers.csv can be found here:
url = "https://raw.githubusercontent.com/Nicholasglim/general-projects/main/datasets/Mall_Customers.csv"
data = pd.read_csv(url)

# Checking whether rows/columns tally with info on kaggle
data.shape

# Previewing first 5 rows of dataset
data.head()

# Summary statistics for each variable
data.describe()

# Checking for missing values
data.isnull().sum()

# Checking for duplicate values
data.duplicated().sum()

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

# Checking data types
data.dtypes

# Converting dtype (object) to (category)
data['gender'] = data['gender'].astype('category')

# Verifying changes
data['gender'].dtype

# Visualise distributions using boxplots. Detected outlier in 'annual_income_k$'
numeric_columns = ['age', 'annual_income_k$', 'spending_score']
for col in numeric_columns:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=data[col])
        plt.title(f'Boxplot of {col}')
        plt.show()

# Handling outlier in 'annual_income_k$' using IQR method
Q1 = data['annual_income_k$'].quantile(0.25)
Q3 = data['annual_income_k$'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identifying outliers
outliers = data[(data['annual_income_k$'] < lower_bound) | (data['annual_income_k$'] > upper_bound)]

print(outliers)

# Filtering out outlier in 'annual_income_k$'
data_filtered = data[(data['annual_income_k$'] >= lower_bound) & (data['annual_income_k$'] <= upper_bound)]

print(data_filtered)
