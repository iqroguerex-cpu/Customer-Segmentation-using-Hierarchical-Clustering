import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    layout="wide"
)

st.title("🛍️ Customer Segmentation using Hierarchical Clustering")

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/iqroguerex-cpu/Customer-Segmentation-using-Hierarchical-Clustering/main/Mall_Customers.csv"
    return pd.read_csv(url)

dataset = load_data()

st.subheader("📊 Raw Dataset")
st.dataframe(dataset)

# Select features
X = dataset.iloc[:, [3, 4]].values

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.header("⚙️ Controls")

n_clusters = st.sidebar.slider("Select Number of Clusters", 2, 10, 5)

linkage_method = st.sidebar.selectbox(
    "Linkage Method",
    ["ward", "complete", "average", "single"]
)

# -----------------------------
# Dendrogram
# -----------------------------
st.subheader("🌳 Dendrogram")

fig1 = plt.figure(figsize=(10, 5))
sch.dendrogram(sch.linkage(X, method=linkage_method))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distance")

st.pyplot(fig1)

# -----------------------------
# Model Training
# -----------------------------
hc = AgglomerativeClustering(
    n_clusters=n_clusters,
    metric='euclidean',
    linkage=linkage_method
)

y_hc = hc.fit_predict(X)

# -----------------------------
# Cluster Visualization
# -----------------------------
st.subheader("🎯 Customer Segments")

fig2 = plt.figure(figsize=(8, 6))

colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple', 'brown']

for i in range(n_clusters):
    plt.scatter(
        X[y_hc == i, 0],
        X[y_hc == i, 1],
        s=80,
        c=colors[i],
        label=f'Cluster {i+1}'
    )

plt.title("Clusters of Customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()

st.pyplot(fig2)

# -----------------------------
# Cluster Insights
# -----------------------------
st.subheader("📈 Cluster Insights")

dataset['Cluster'] = y_hc

summary = dataset.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)']].mean()

st.dataframe(summary)

# -----------------------------
# Download Option
# -----------------------------
csv = dataset.to_csv(index=False).encode('utf-8')

st.download_button(
    label="⬇️ Download Clustered Data",
    data=csv,
    file_name='clustered_customers.csv',
    mime='text/csv'
)
