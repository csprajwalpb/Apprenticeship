# 🏥 Hospital Emergency Classification using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [120, 160],
    [115, 155],
    [70, 110],
    [75, 105],
    [90, 120]
])

y = np.array(['Critical', 'Critical', 'Stable', 'Stable', 'Stable'])

# New Patient
new_patient = np.array([[100, 130]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
predicted_condition = model.predict(new_patient)
print(" Predicted Condition:", predicted_condition[0])
