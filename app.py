import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Startup KPI Dashboard", layout="wide")

st.title("📊 Startup KPI Tracker")
st.markdown("Upload your KPI CSV to see metrics, growth, and insights.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Calculate KPIs
    df["Revenue Growth (%)"] = df["Revenue"].pct_change() * 100
    df["User Growth (%)"] = df["Users"].pct_change() * 100
    df["Burn Rate"] = df["Expenses"]
    df["Net Income"] = df["Revenue"] - df["Expenses"]

    st.subheader("📈 KPI Summary")
    st.dataframe(df.style.format("{:.2f}", subset=["User Growth (%)", "Revenue Growth (%)", "Net Income"]))

    # Revenue and Net Income Line Chart
    st.subheader("💵 Revenue & Net Income Over Time")
    fig1, ax1 = plt.subplots()
    ax1.plot(df["Week"], df["Revenue"], marker='o', label="Revenue")
    ax1.plot(df["Week"], df["Net Income"], marker='s', label="Net Income")
    ax1.set_xlabel("Week")
    ax1.set_ylabel("Amount ($)")
    ax1.set_title("Revenue & Net Income")
    ax1.grid(True)
    ax1.legend()
    st.pyplot(fig1)

    # User Growth Bar Chart
    st.subheader("📊 User Growth (%)")
    fig2, ax2 = plt.subplots()
    ax2.bar(df["Week"], df["User Growth (%)"], color='orange')
    ax2.set_xlabel("Week")
    ax2.set_ylabel("Growth %")
    ax2.set_title("User Growth Over Time")
    ax2.grid(True)
    st.pyplot(fig2)
else:
    st.info("⬆️ Upload a CSV file with Week, Users, Revenue, and Expenses columns.")
