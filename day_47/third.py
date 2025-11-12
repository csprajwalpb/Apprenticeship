# 🧍 Health Check – Diabetes Prediction using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [150, 30],
    [160, 32],
    [85, 18],
    [90, 20],
    [120, 25]
])

y = np.array(['Yes', 'Yes', 'No', 'No', 'No'])

# New Patient
new_patient = np.array([[140, 28]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
predicted = model.predict(new_patient)
print("🩺 Predicted Diabetes:", predicted[0])
