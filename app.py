import joblib
import numpy as np
import pandas as pd
import streamlit as st

DATA_PATH = "data/processed/customer_segments.csv"
MODEL_DIR = "models/"

NUMERIC_FEATURES = [
    "Income", "Recency", "NumDealsPurchases", "NumWebPurchases",
    "NumCatalogPurchases", "NumStorePurchases", "NumWebVisitsMonth",
    "Complain", "Response", "Age", "Customer_Tenure_Days",
    "Total_Spending", "Total_Children",
]

# based on the real cluster_summary() numbers from the notebook
CLUSTER_STRATEGY = {
    0: ("Budget Families", "Lowest income/spending, mostly partnered with kids, weakest campaign response.",
        "Discount bundles and family-value offers."),
    1: ("Established Shoppers", "Mid-to-high income and spending, mostly partnered, shop in-store more.",
        "Loyalty programs and in-store promos."),
    2: ("Premium High-Value", "Highest income and spending, fewest kids, best campaign response.",
        "Top priority for new campaigns - best ROI."),
    3: ("Budget Singles", "Low income/spending, living alone, moderate response.",
        "Cheap entry offers and digital engagement."),
}


def load_data():
    try:
        return pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        return None


def load_model(name):
    try:
        return joblib.load(MODEL_DIR + name + ".pkl")
    except FileNotFoundError:
        return None


def predict_cluster(inputs, kmeans, scaler, encoder, pca):
    numeric_vals = [[inputs[col] for col in NUMERIC_FEATURES]]
    cat_row = pd.DataFrame([[inputs["Education"], inputs["Living_With"]]],
                            columns=["Education", "Living_With"])
    encoded = encoder.transform(cat_row).toarray()

    row = np.hstack([numeric_vals, encoded])
    row = scaler.transform(row)
    row = pca.transform(row)
    return int(kmeans.predict(row)[0])


def show_strategy(cluster_id):
    if cluster_id in CLUSTER_STRATEGY:
        name, summary, rec = CLUSTER_STRATEGY[cluster_id]
        st.write("Cluster", cluster_id, "-", name)
        st.write(summary)
        st.write("Recommendation:", rec)


def show_dashboard(df):
    st.header("Business Insights")

    if df is None:
        st.warning("No data found. Run the notebook first to create customer_segments.csv")
        return

    st.subheader("Marketing Recommendations")
    for cid in sorted(df["cluster"].unique()):
        show_strategy(int(cid))

    summary = df.groupby("cluster")[["Income", "Total_Spending", "Response"]].mean()
    counts = df["cluster"].value_counts().sort_index()

    st.subheader("Average Spending per Cluster")
    st.bar_chart(summary["Total_Spending"])

    st.subheader("Average Income per Cluster")
    st.bar_chart(summary["Income"])

    st.subheader("Campaign Response Rate per Cluster (%)")
    st.bar_chart(summary["Response"] * 100)

    st.subheader("Cluster Size")
    st.bar_chart(counts)

    st.subheader("Full Summary Table")
    st.write(summary)


def show_predict_page(df, kmeans, scaler, encoder, pca):
    st.header("Predict a Customer's Segment")

    if kmeans is None or scaler is None or encoder is None or pca is None:
        st.warning("Model files are missing from the models folder. Add them to enable prediction.")
        return

    income = st.number_input("Annual Income ($)", min_value=0, value=50000, step=1000)
    age = st.number_input("Age", min_value=18, max_value=100, value=40)
    recency = st.number_input("Days Since Last Purchase", min_value=0, value=30)
    tenure = st.number_input("Customer Tenure (days)", min_value=0, value=365)
    spending = st.number_input("Total Spending ($, last 2 years)", min_value=0, value=500)
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    deals = st.number_input("Deal Purchases", min_value=0, value=2)
    web = st.number_input("Web Purchases", min_value=0, value=3)
    catalog = st.number_input("Catalog Purchases", min_value=0, value=2)
    store = st.number_input("Store Purchases", min_value=0, value=5)
    web_visits = st.number_input("Web Visits per Month", min_value=0, value=5)
    education = st.selectbox("Education", ["Undergraduate", "Graduate", "Postgraduate"])
    living_with = st.selectbox("Living Situation", ["Alone", "Partner"])
    complain = st.checkbox("Filed a complaint in the last 2 years")
    responded = st.checkbox("Responded to the last marketing campaign")

    if st.button("Predict Segment"):
        inputs = {
            "Income": income, "Recency": recency, "NumDealsPurchases": deals,
            "NumWebPurchases": web, "NumCatalogPurchases": catalog, "NumStorePurchases": store,
            "NumWebVisitsMonth": web_visits, "Complain": int(complain), "Response": int(responded),
            "Age": age, "Customer_Tenure_Days": tenure, "Total_Spending": spending,
            "Total_Children": children, "Education": education, "Living_With": living_with,
        }
        cluster_id = predict_cluster(inputs, kmeans, scaler, encoder, pca)
        st.success("Predicted Segment: Cluster " + str(cluster_id))
        show_strategy(cluster_id)


def main():
    st.title("Customer Segmentation with Marketing Insights")

    df = load_data()
    kmeans = load_model("kmeans_model")
    scaler = load_model("scaler")
    encoder = load_model("encoder")
    pca = load_model("pca")

    page = st.sidebar.radio("Go to", ["Dashboard", "Predict Segment"])

    if page == "Dashboard":
        show_dashboard(df)
    else:
        show_predict_page(df, kmeans, scaler, encoder, pca)


main()
