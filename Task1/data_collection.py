import pandas as pd

# Load dataset directly from internet
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Save locally
df.to_csv('../data/tips.csv', index=False)

print("\nData downloaded and saved successfully!")