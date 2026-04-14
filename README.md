# 🛍️ Customer Segmentation Dashboard (Hierarchical Clustering)

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![License](https://img.shields.io/badge/License-MIT-green)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Open%20App-brightgreen?logo=rocket)](https://hrw5guwe5h6p9fcd5khlf8.streamlit.app/)

</p>

---

## 🚀 Overview

An interactive **Customer Segmentation Dashboard** built with Streamlit that uses **Hierarchical Clustering (Agglomerative Clustering)** to group customers based on income and spending behavior.

The dashboard provides **dendrogram visualization, cluster analysis, and insights**, helping understand customer segmentation patterns.

---

## ✨ Features

* 🌳 Dendrogram visualization for hierarchical clustering
* 🎛️ Adjustable parameters:

  * Number of clusters
  * Linkage method (ward, complete, average, single)
* 📊 Cluster visualization (scatter plot)
* 📈 Cluster insights (mean income & spending)
* 📂 Dataset preview
* 📥 Download clustered dataset

---

## 🛠️ Tech Stack

* Python 3.x
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* SciPy

---

## 📂 Project Structure

```bash
.
├── app.py
├── Mall_Customers.csv (GitHub hosted)
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup

### 1. Add dataset to GitHub

Upload your dataset to your repository.

### 2. Get raw file link

Example:

```bash
https://raw.githubusercontent.com/username/repo/main/Mall_Customers.csv
```

### 3. Update in code

```python
url = "your-raw-github-link"
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 📊 Model Details

* Algorithm: **Agglomerative Hierarchical Clustering**
* Distance Metric: Euclidean
* Linkage Methods:

  * Ward
  * Complete
  * Average
  * Single

---

## 📈 Visualizations

* 🌳 Dendrogram (hierarchical structure)
* 🎯 Cluster scatter plot
* 📊 Cluster summary table

---

## 🧠 How It Works

1. Dataset is loaded from GitHub
2. Features (Income & Spending Score) are selected
3. Dendrogram helps visualize cluster formation
4. Agglomerative clustering assigns cluster labels
5. Results are displayed with insights

---

## 📁 Dataset

The dataset (`Mall_Customers.csv`) includes:

* CustomerID
* Gender
* Age
* Annual Income (k$)
* Spending Score (1–100)

---

## 🎛️ Controls

* **Cluster Slider** → Adjust number of clusters
* **Linkage Method Selector** → Change clustering strategy

---

## 📥 Export Feature

Download the dataset with assigned cluster labels directly from the dashboard.

---

## 🚀 Deployment

Deploy easily using **Streamlit Cloud**:

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Create new app
4. Deploy 🎉

---

## 🔮 Future Improvements

* 📊 Compare with K-Means clustering
* 📉 PCA / dimensionality reduction
* 📊 Interactive Plotly visualizations
* 🧠 Automatic cluster labeling
* 📊 3D cluster visualization

---

## 👨‍💻 Author

**Chinmay V Chatradamath**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
