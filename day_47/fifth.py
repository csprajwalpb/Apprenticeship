# 🎓 Student Performance Prediction using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [10, 90],
    [8, 85],
    [2, 40],
    [3, 45],
    [5, 60]
])

y = np.array(['Pass', 'Pass', 'Fail', 'Fail', 'Fail'])

# New Student
new_student = np.array([[6, 80]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
predicted_result = model.predict(new_student)
print("🎯 Predicted Result:", predicted_result[0])
