import pandas as pd

# Load dataset
df = pd.read_csv("NFHS-5-KA-Karnataka.csv")

# Filter for Bagalkot district
district_data = df[df['District'] == 'Bagalkot']

# Display first 5 rows
print(district_data.head())

# Save filtered data to new CSV
district_data.to_csv("Bagalkot_health_data.csv", index=False)

df.info()


df.describe()
