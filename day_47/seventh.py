# 🚗 Car Purchase Decision using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [25, 30],
    [35, 70],
    [45, 80],
    [20, 25],
    [30, 40]
])

y = np.array(['No', 'Yes', 'Yes', 'No', 'No'])

# New Customer
new_customer = np.array([[40, 75]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
predicted = model.predict(new_customer)
print(" Predicted Decision:", predicted[0])
