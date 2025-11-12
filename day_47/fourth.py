# 📱 Mobile Plan Recommendation using KNN
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = np.array([
    [10, 500],
    [8, 400],
    [2, 100],
    [3, 150],
    [6, 350]
])

y = np.array(['Premium', 'Premium', 'Basic', 'Basic', 'Premium'])

# New User
new_user = np.array([[4, 200]])

# KNN model
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# Prediction
predicted_plan = model.predict(new_user)
print("📶 Recommended Plan:", predicted_plan[0])
