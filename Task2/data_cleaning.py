import pandas as pd

# Load dataset
df = pd.read_csv('../data/tips.csv')

print("Original Data:")
print(df.head())

# 🔹 Step 1: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 🔹 Step 2: Remove duplicates
duplicates = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")

df = df.drop_duplicates()

# 🔹 Step 3: Standardize text (clean strings)
df['sex'] = df['sex'].str.strip().str.lower()
df['smoker'] = df['smoker'].str.strip().str.lower()
df['day'] = df['day'].str.strip().str.lower()
df['time'] = df['time'].str.strip().str.lower()

# 🔹 Step 4: Rename columns (optional cleaning)
df.columns = df.columns.str.lower()

# 🔹 Step 5: Check data types
print("\nData Types:")
print(df.dtypes)

# 🔹 Step 6: Save cleaned data
df.to_csv('../data/cleaned_data.csv', index=False)

print("\nData cleaning completed successfully!")