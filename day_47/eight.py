# 💻 Software Bug Severity Classification using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [50, 1],
    [80, 2],
    [200, 5],
    [250, 6],
    [100, 2]
])

y = np.array(['Minor', 'Minor', 'Critical', 'Critical', 'Minor'])

# New Bug
new_bug = np.array([[220, 5]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
predicted_severity = model.predict(new_bug)
print(" Predicted Severity:", predicted_severity[0])
