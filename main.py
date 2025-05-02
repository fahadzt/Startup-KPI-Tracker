import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Calculate KPIs
df["Revenue Growth (%)"] = df["Revenue"].pct_change() * 100
df["User Growth (%)"] = df["Users"].pct_change() * 100
df["Burn Rate"] = df["Expenses"]
df["Net Income"] = df["Revenue"] - df["Expenses"]

# Print report
print("📊 Weekly Startup KPI Report")
print(df[["Week", "Users", "Revenue", "Expenses", "User Growth (%)", "Revenue Growth (%)", "Burn Rate", "Net Income"]])

# Save to CSV
df.to_csv("kpi_report.csv", index=False)
import matplotlib.pyplot as plt

# Line chart for Revenue
plt.figure(figsize=(8, 5))
plt.plot(df["Week"], df["Revenue"], marker='o', label="Revenue")
plt.plot(df["Week"], df["Net Income"], marker='s', label="Net Income")
plt.title("Weekly Revenue & Net Income")
plt.xlabel("Week")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("revenue_net_income_chart.png")
plt.show()

# Bar chart for User Growth
plt.figure(figsize=(8, 5))
plt.bar(df["Week"], df["User Growth (%)"], color='orange')
plt.title("Weekly User Growth %")
plt.xlabel("Week")
plt.ylabel("Growth %")
plt.grid(True)
plt.tight_layout()
plt.savefig("user_growth_chart.png")
plt.show()
