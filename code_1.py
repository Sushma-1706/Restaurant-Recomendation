import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset .csv")

# Show the first few rows
print(df.head())

# Check info and missing values
print("\nData Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
