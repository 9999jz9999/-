# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:42:49 2024

@author: kkjj1
"""
#使用 matplotlib library 根據 iris 資料庫的前兩個欄位繪製散佈圖，不同種類以不同的顏色標記。
# Import necessary libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data[:, :2]  # Select the first two columns
y = iris.target
target_names = iris.target_names

# Create a scatter plot
plt.figure(figsize=(8, 6))
colors = ['navy', 'turquoise', 'darkorange']

for i, color, target_name in zip(range(len(target_names)), colors, target_names):
    plt.scatter(X[y == i, 0], X[y == i, 1], color=color, label=target_name)

# Add title and labels
plt.title('Scatter plot of Iris dataset')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.legend()
plt.show()


#________________________________________________

#使用 matplotlib library 根據 kmeans 模型的預測結果繪製混淆矩陣。

# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Calculate the confusion matrix
cm = confusion_matrix(y, y_kmeans)

# Since k-means clustering doesn't assign the same labels as the original, we need to match them
def match_labels(true_labels, pred_labels):
    mapping = {}
    for true in np.unique(true_labels):
        mask = true_labels == true
        pred = pred_labels[mask]
        new_label = np.bincount(pred).argmax()
        mapping[true] = new_label
    new_pred_labels = np.array([mapping[label] for label in pred_labels])
    return new_pred_labels

# Map the kmeans labels to the true labels
y_kmeans_mapped = match_labels(y, y_kmeans)

# Recalculate the confusion matrix with the mapped labels
cm_mapped = confusion_matrix(y, y_kmeans_mapped)

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm_mapped, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title('Confusion Matrix for KMeans Clustering on Iris Dataset')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()
