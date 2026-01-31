# Q1 - 
import pandas as pd

# Replace 'your_file_path.xlsx' with the path to your Excel file
df = pd.read_excel('Lab\Lab 11&12\data.xlsx')

# print(df)

# Q2
df.to_csv('new.csv', index=False)

# Q3
# Specify the column names
col_names = ['ticker', 'eps', 'revenue', 'price', 'people']

# Read the CSV file with the specified column names
df = pd.read_csv('new.csv', names=col_names)

# print(df)

# Q4
# import pandas as pd
import numpy as np

# Assuming that 'df' is your DataFrame

# Convert 'not available' or 'n.a.' values to NaN
df.replace(['not available', 'n.a.'], np.nan, inplace=True)

# Convert negative revenues to NaN
df['revenue'] = df['revenue'].mask(df['revenue'] < 0)

# print(df)

# Q5
df = df.fillna(0)
# print(df)

# Q6-
def replace_na(row):
    if row['ticker'] == 'WMT' and row['people'] == 'n.a':
        return 'Sam Walton'
    else:
        return row['people']

# Apply the function to the DataFrame
df['people'] = df.apply(replace_na, axis=1)
print(df)

