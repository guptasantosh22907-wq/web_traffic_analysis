
import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Pages and user types
pages = ["Home", "About", "Products", "Contact"]
user_types = ["New", "Returning"]

# Generate 50 days ending at Dec 31, 2025
dates = pd.date_range(end="2025-12-31", periods=50)

rows = []

# Generate data
for date in dates:
    for page in pages:
        visits = np.random.randint(50, 500)  # Random visits between 50–500
        user_type = np.random.choice(user_types)
        rows.append([date.date(), page, visits, user_type])

# Create DataFrame
data = pd.DataFrame(rows, columns=["Date", "Page", "Visits", "UserType"])

# Save to CSV
data.to_csv("web_traffic_dec2025.csv", index=False)
print(f" CSV generated with {len(data)} rows for December 2025 as 'web_traffic_dec2025.csv'")
# Step 2: Load Web Traffic CSV and Check Data
import pandas as pd

# Load CSV file
file_path = r"C:\Users\User\PycharmProjects\web_traffic_analysis\web_traffic_dec2025.csv"
data = pd.read_csv(file_path)

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Quick look at first 5 rows
print(" First 5 rows:")
print(data.head())

# Dataset info
print("\n Dataset info:")
print(data.info())

# Missing values check
print("\n Missing values per column:")
print(data.isnull().sum())

import matplotlib.pyplot as plt

# 1️⃣ Group data by Page and sum visits
page_visits = data.groupby('Page')['Visits'].sum()
print("\n Total Visits per Page:")
print(page_visits)

# 2️⃣ Create a bar chart
page_visits.plot(kind='bar', color='skyblue', title='Total Visits per Page')
plt.ylabel('Visits')
plt.xlabel('Page')
plt.xticks(rotation=0)
plt.show()
# 1️⃣ Group data by Date and sum visits
daily_visits = data.groupby('Date')['Visits'].sum()
print("\n Daily Visits Trend:")
print(daily_visits)

# 2️⃣ Create a line chart
daily_visits.plot(kind='line', marker='o', color='green', title='Daily Visits Trend')
plt.ylabel('Visits')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
# 1️⃣ Group data by Date and sum visits
daily_visits = data.groupby('Date')['Visits'].sum()
print("\n Daily Visits Trend:")
print(daily_visits)

# 1️⃣ Group data by UserType and sum visits
user_visits = data.groupby('UserType')['Visits'].sum()
print("\n Visits by User Type:")
print(user_visits)

# 2️⃣ Create a pie chart
user_visits.plot(kind='pie', autopct='%1.1f%%', title='Visits by User Type', colors=['#66b3ff','#ff9999'])
plt.ylabel('')  # Remove ylabel for cleaner look
plt.show()
