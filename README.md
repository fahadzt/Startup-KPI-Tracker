# 📊 Startup KPI Tracker

A lightweight Python dashboard that helps startups visualize and track weekly growth metrics like revenue, user base, and burn rate — built with Pandas, Matplotlib, and Streamlit.

---

## 🚀 Live Demo

👉 [Try the app on Streamlit Cloud](https://fahadzt-startup-kpi-tracker.streamlit.app)

---

## 📌 Features

- Upload your own weekly KPI CSV
- Automatically calculates:
  - 📈 Revenue Growth %
  - 👥 User Growth %
  - 🔥 Burn Rate
  - 💰 Net Income
- Generates visual charts:
  - Revenue & Net Income over time
  - User Growth bar chart
- Clean, interactive UI using Streamlit

---

## 📂 Sample Input Format

Your CSV should look like this:

```csv
Week,Users,Revenue,Expenses
1,100,500,300
2,130,700,400
3,160,850,500
4,200,1000,550
