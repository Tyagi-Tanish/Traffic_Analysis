import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Traffic Analytics Dashboard", layout="wide")

st.title("🚦 Smart Traffic & Road Safety Analytics Dashboard")

# Load data
df = pd.read_csv("data/traffic_accidents.csv")

# ==============================
# Sidebar Filters
# ==============================
st.sidebar.header("Filters")

area_filter = st.sidebar.multiselect(
    "Select Area",
    options=df["Area"].unique(),
    default=df["Area"].unique()
)

severity_filter = st.sidebar.multiselect(
    "Select Severity",
    options=df["Severity"].unique(),
    default=df["Severity"].unique()
)

filtered_df = df[
    (df["Area"].isin(area_filter)) &
    (df["Severity"].isin(severity_filter))
]

# ==============================
# Dashboard Metrics
# ==============================
col1, col2, col3 = st.columns(3)

col1.metric("Total Accidents", len(filtered_df))
col2.metric("High Severity Cases", len(filtered_df[filtered_df["Severity"] == "High"]))
col3.metric("Unique Areas", filtered_df["Area"].nunique())

st.divider()

# ==============================
# Charts
# ==============================
st.subheader("📍 Accident Count by Area")
area_counts = filtered_df["Area"].value_counts()
fig1, ax1 = plt.subplots()
area_counts.plot(kind="bar", ax=ax1)
st.pyplot(fig1)

st.subheader("⚠️ Accident Severity Distribution")
severity_counts = filtered_df["Severity"].value_counts()
fig2, ax2 = plt.subplots()
severity_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

st.subheader("🚨 Top Causes of Accidents")
cause_counts = filtered_df["Cause"].value_counts()
fig3, ax3 = plt.subplots()
cause_counts.plot(kind="bar", ax=ax3)
st.pyplot(fig3)

st.subheader("⏰ Accidents by Hour")
filtered_df["Hour"] = pd.to_datetime(filtered_df["Time"]).dt.hour
hour_counts = filtered_df["Hour"].value_counts().sort_index()
fig4, ax4 = plt.subplots()
hour_counts.plot(kind="line", marker="o", ax=ax4)
st.pyplot(fig4)
