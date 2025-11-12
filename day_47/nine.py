# 🍔 Food Recommendation using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [700, 40],
    [650, 35],
    [200, 5],
    [250, 10],
    [500, 25]
])

y = np.array(['Fast Food', 'Fast Food', 'Healthy', 'Healthy', 'Fast Food'])

# New Food Item
new_food = np.array([[300, 15]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
predicted_type = model.predict(new_food)
print("Predicted Food Type:", predicted_type[0])
