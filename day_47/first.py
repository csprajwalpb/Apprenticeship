# 🎬 Movie Genre Prediction using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [9, 1],
    [8, 2],
    [1, 9],
    [2, 8],
    [6, 3]
])

y = np.array(['Action', 'Action', 'Romance', 'Romance', 'Action'])

# New Movie
new_movie = np.array([[3, 7]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Predict
predicted_genre = model.predict(new_movie)
print(" Predicted Genre:", predicted_genre[0])
