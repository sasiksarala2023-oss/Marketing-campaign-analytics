# Marketing Campaign Analytics - End-to-End Demo
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load dataset
data = pd.read_csv("marketing_campaign_data.csv")

# 2. Data Cleaning & Derived Features
data["Dt_Customer"] = pd.to_datetime(data["Dt_Customer"])
data["Age"] = 2026 - data["Year_Birth"]
data["Children"] = data["Kidhome"] + data["Teenhome"]
data["Total_Spend"] = data[["MntWines","MntFruits","MntMeatProducts",
                            "MntFishProducts","MntSweetProducts","MntGoldProds"]].sum(axis=1)
data["Total_Purchases"] = data[["NumDealsPurchases","NumWebPurchases",
                                "NumCatalogPurchases","NumStorePurchases"]].sum(axis=1)

# 3. Exploratory Data Analysis (EDA)

# Age distribution
plt.figure(figsize=(8,5))
sns.histplot(data["Age"], bins=30, kde=True)
plt.title("Customer Age Distribution")

# Income distribution
plt.figure(figsize=(8,5))
sns.histplot(data["Income"], bins=30, kde=True)
plt.title("Income Distribution")

# Average spend per product category
spend_cols = ["MntWines","MntFruits","MntMeatProducts",
              "MntFishProducts","MntSweetProducts","MntGoldProds"]
data[spend_cols].mean().plot(kind="bar", figsize=(8,5))
plt.title("Average Spend per Product Category")

# Response vs Age
plt.figure(figsize=(8,5))
sns.boxplot(x="Response", y="Age", data=data)
plt.title("Age vs Campaign Response")

# Response vs Income
plt.figure(figsize=(8,5))
sns.boxplot(x="Response", y="Income", data=data)
plt.title("Income vs Campaign Response")

# Scatter: Income vs Total Spend by Response
plt.figure(figsize=(8,5))
sns.scatterplot(x="Income", y="Total_Spend", hue="Response", data=data)
plt.title("Income vs Total Spend by Response")

# 4. Segmentation Rules
data["HighIncome"] = np.where(data["Income"] > 75000, 1, 0)
data["YoungCustomer"] = np.where(data["Age"] < 30, 1, 0)
data["Responder"] = data["Response"]
data["HighWebEngagement"] = np.where(data["NumWebVisitsMonth"] > 5, 1, 0)
data["FamilyCustomer"] = np.where(data["Children"] > 0, 1, 0)
threshold = data["Total_Spend"].quantile(0.9)
data["HighSpender"] = np.where(data["Total_Spend"] > threshold, 1, 0)

# 5. KPI Example: Average Spend & Response Rate per Segment
segment_summary = data.groupby("HighIncome")[["Total_Spend","Response"]].mean()
print("Segment Summary (High Income vs Others):")
print(segment_summary)
import matplotlib.pyplot as plt
import seaborn as sns

# Create a figure with multiple subplots (2 rows, 3 columns)
fig, axes = plt.subplots(2, 3, figsize=(18,10))

# Age distribution
sns.histplot(data["Age"], bins=30, kde=True, ax=axes[0,0])
axes[0,0].set_title("Age Distribution")

# Income distribution
sns.histplot(data["Income"], bins=30, kde=True, ax=axes[0,1])
axes[0,1].set_title("Income Distribution")

# Average spend per product category
spend_cols = ["MntWines","MntFruits","MntMeatProducts",
              "MntFishProducts","MntSweetProducts","MntGoldProds"]
data[spend_cols].mean().plot(kind="bar", ax=axes[0,2])
axes[0,2].set_title("Average Spend per Product Category")

# Response vs Age
sns.boxplot(x="Response", y="Age", data=data, ax=axes[1,0])
axes[1,0].set_title("Age vs Response")

# Response vs Income
sns.boxplot(x="Response", y="Income", data=data, ax=axes[1,1])
axes[1,1].set_title("Income vs Response")

# Scatter: Income vs Total Spend by Response
sns.scatterplot(x="Income", y="Total_Spend", hue="Response", data=data, ax=axes[1,2])
axes[1,2].set_title("Income vs Total Spend")

# Adjust layout so titles/labels don’t overlap
plt.tight_layout()
fig.suptitle("Marketing Campaign EDA Overview", fontsize=18, fontweight="bold")
# 🔑 Save the entire figure as PNG or PDF
fig.savefig("marketing_analysis.png", dpi=300)   # saves as PNG
fig.savefig("marketing_analysis.pdf")            # saves as PDF
plt.show()
