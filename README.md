#  Customer Segmentation with Marketing Insights  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://customer-segmentation-with-marketing-insights-y9kuryeqhsqwtzso.streamlit.app/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/omermohd327-svg/Customer-Segmentation-with-Marketing-Insights/blob/main/notebook/customer_segmentation.ipynb)

**Live app:** http://customer-segmentation-with-marketing-insights-y9kuryeqhsqwtzso.streamlit.app/

##  Business Problem

Modern businesses collect vast amounts of customer data but often struggle to understand customer behavior and spending patterns.

Treating all customers the same leads to:

- Inefficient marketing campaigns
- Poor customer retention
- Low personalization
- Wasted marketing budget

This project uses Machine Learning to identify distinct customer groups and generate actionable marketing insights that can improve business decision-making.

---

##  Business Objective

The primary objectives of this project are:

- Identify meaningful customer segments
- Understand customer spending behavior
- Improve marketing effectiveness
- Enable personalized campaigns
- Increase customer retention and lifetime value
- Generate actionable business insights

---

##  Dataset

### Source

Customer Personality Analysis (Marketing Campaign) Dataset

### Raw Features (`data/raw/marketing_campaign.csv`)

- ID, Year_Birth, Education, Marital_Status
- Income, Kidhome, Teenhome, Dt_Customer, Recency
- MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds
- NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth
- Complain, Response

### Engineered Features (`data/processed/customer_segments.csv`)

- Age (from Year_Birth)
- Customer_Tenure_Days (from Dt_Customer)
- Total_Spending (sum of all Mnt* columns)
- Total_Children (Kidhome + Teenhome)
- Education collapsed into Undergraduate / Graduate / Postgraduate
- Living_With (Partner / Alone, derived from Marital_Status)
- Income, Recency, Response, and the final cluster label

These features are used to discover hidden customer patterns and group similar customers together.

---

##  Exploratory Data Analysis (EDA)

Before clustering, exploratory analysis was performed to understand customer demographics and spending behavior.

![EDA Distribution](images/eda_distributions.png)

### Key Observations

- Annual income varies significantly across customers.
- Spending scores are distributed across multiple customer groups.
- Customer behavior appears heterogeneous, suggesting natural segmentation opportunities.

---

##  Correlation Analysis

A correlation heatmap was generated to understand relationships between customer attributes.

![Correlation Heatmap](images/heatmap.png)

### Insights

- Some features show weak relationships, indicating that customer behavior is influenced by multiple factors.
- Clustering can help uncover patterns that traditional correlation analysis cannot reveal.

---

##  Machine Learning Workflow

The project follows the following pipeline:

```text
Customer Data
        ↓
Exploratory Data Analysis
        ↓
Feature Selection
        ↓
Feature Scaling
        ↓
Optimal Cluster Selection
        ↓
K-Means Clustering
        ↓
Cluster Validation
        ↓
Customer Segmentation
        ↓
Business Insights
```

---

##  Data Preprocessing

The following preprocessing steps were performed:

- Data inspection
- Feature selection
- Feature scaling using StandardScaler
- Preparation for clustering algorithms

Feature scaling is essential because clustering algorithms rely on distance-based calculations.

---

##  Finding the Optimal Number of Clusters

The Elbow Method was used to identify the optimal number of clusters.

### Elbow Curve

![Elbow Curve](images/elbow_curve.png)

---

##  Cluster Validation using Silhouette Score

To validate cluster quality, Silhouette Analysis was performed.

### Silhouette Scores

![Silhouette Scores](images/silhouette_scores.png)


---

##  Customer Segmentation using K-Means

After determining the optimal number of clusters, K-Means Clustering was applied.

---

##  Customer Segment Visualization

To visualize clusters effectively, PCA (Principal Component Analysis) was used.

### PCA Cluster Visualization

![PCA Clusters](images/pca_clusters.png)

### Observation

Distinct customer groups can be observed, indicating meaningful segmentation within the dataset.

---

##  Customer Segment Profiles

The resulting clusters were analyzed to understand customer behavior patterns.

![Cluster Profiles](images/clusters_profiles.png)

---

##  Segment Interpretation


###  Cluster 0 — Budget Families

**Characteristics**

- Lowest income (~$35.6k) and lowest spending (~$131)
- Mostly partnered, with children
- Weakest campaign response (6.2%)

**Business Strategy**

- Discount bundles
- Family-value offers
- Low priority for premium campaign spend

---

###  Cluster 1 — Established Shoppers

**Characteristics**

- Mid-to-high income (~$59.9k) and mid-to-high spending (~$796)
- Mostly partnered, prefer in-store over web purchases
- Moderate campaign response (17.4%)

**Business Strategy**

- Loyalty programs
- In-store promotions
- Targeted campaigns to grow share of wallet

---

###  Cluster 2 — Premium High-Value

**Characteristics**

- Highest income (~$74.7k) and highest spending (~$1,306)
- Fewest children
- Best campaign response (23.8%)

**Business Strategy**

- Top priority for new campaigns
- VIP memberships and early access to products
- Premium, high-touch experiences

---

###  Cluster 3 — Budget Singles

**Characteristics**

- Low income (~$38.1k) and low spending (~$183)
- Living alone
- Moderate campaign response (13.8%)

**Business Strategy**

- Low-cost entry offers
- Digital engagement to build long-term value
- Cost-effective marketing


---

##  Agglomerative Clustering (Comparison)

In addition to K-Means, Agglomerative Clustering was explored as an alternative clustering approach.

### Agglomerative Clustering

![Agglomerative Clustering](images/agglomerative_clustering.png)

### Purpose

Comparing multiple clustering techniques helps evaluate segmentation consistency and cluster quality.

---

##  Business Recommendations

Based on segmentation results:

### VIP Customers

- Reward loyalty
- Offer exclusive benefits
- Increase customer lifetime value

### Opportunity Customers

- Encourage spending through personalized campaigns
- Improve customer engagement

### Budget Customers

- Focus on affordability
- Promote value-driven offerings

### Regular Customers

- Maintain engagement through targeted promotions
- Encourage repeat purchases

---

##  Key Insights

- Customer behavior naturally forms distinct groups.
- Income alone does not determine spending behavior.
- High-income customers are not always high spenders.
- Segmentation enables more effective marketing strategies.
- Data-driven customer understanding improves business outcomes.

---


##  How to Run

### Clone the Repository

```bash
git clone https://github.com/omermohd327-svg/Customer-Segmentation-with-Marketing-Insights.git
cd Customer-Segmentation-with-Marketing-Insights
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebook/customer_segmentation.ipynb
```
### Run locally
```bash
streamlit run app.py
```
---

##  Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- K-Means Clustering
- Agglomerative Clustering
- StandardScaler
- PCA

---

##  Project Structure

```text
Customer-Segmentation-with-Marketing-Insights/
│
├── data/
│   ├── raw/
│   │   └── marketing_campaign.csv
│   └── processed/
│       └── customer_segments.csv
|
├── notebook/
│   └── customer_segmentation.ipynb
│
├── models/
|   ├── encoder.pkl
│   ├── scaler.pkl
│   ├── pca.pkl
│   └── kmeans_model.pkl
│
├── images/
│   ├── pca_clusters.png
│   ├── elbow_curve.png
│   ├── silhouette_scores.png
│   ├── agglomerative_clustering.png
│   ├── clusters_profiles.png
│   ├── heatmap.png
│   └── eda_distribution.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Conclusion

This project demonstrates how Machine Learning can transform raw customer data into meaningful business intelligence.
By identifying distinct customer segments, businesses can improve marketing efficiency, personalize customer experiences, increase retention, and make more informed strategic decisions.

By identifying distinct customer segments, businesses can improve marketing efficiency, personalize customer experiences, increase retention, and make more informed strategic decisions.
