import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/traffic_accidents.csv")

# ================================
# Accident count by area
# ================================
area_counts = df["Area"].value_counts()
plt.figure()
area_counts.plot(kind="bar", title="Accident Count by Area")
plt.xlabel("Area")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("accidents_by_area.png")
plt.close()

# ================================
# Accident severity distribution
# ================================
severity_counts = df["Severity"].value_counts()
plt.figure()
severity_counts.plot(kind="pie", autopct="%1.1f%%", title="Accident Severity Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("severity_distribution.png")
plt.close()

# ================================
# Accident causes
# ================================
cause_counts = df["Cause"].value_counts()
plt.figure()
cause_counts.plot(kind="bar", title="Top Causes of Accidents")
plt.xlabel("Cause")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("accident_causes.png")
plt.close()

# ================================
# Peak accident hours
# ================================
df["Hour"] = pd.to_datetime(df["Time"]).dt.hour
hour_counts = df["Hour"].value_counts().sort_index()
plt.figure()
hour_counts.plot(kind="line", marker="o", title="Accidents by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("accidents_by_hour.png")
plt.close()

print("Analysis complete. Charts saved successfully.")
