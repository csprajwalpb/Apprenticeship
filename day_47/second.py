# 🏡 House Price Category Prediction using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [3500, 4],
    [3000, 3],
    [1500, 2],
    [1200, 2],
    [2000, 3]
])

y = np.array(['Expensive', 'Expensive', 'Affordable', 'Affordable', 'Affordable'])

# New House
new_house = np.array([[2200, 3]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
predicted_category = model.predict(new_house)
print("🏠 Predicted Category:", predicted_category[0])
