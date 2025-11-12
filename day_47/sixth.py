# 🛒 Customer Segmentation using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [90, 80],
    [85, 75],
    [20, 15],
    [25, 20],
    [60, 50]
])

y = np.array(['High', 'High', 'Low', 'Low', 'High'])

# New Customer
new_customer = np.array([[30, 25]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
predicted_type = model.predict(new_customer)
print("🧾 Predicted Customer Type:", predicted_type[0])
