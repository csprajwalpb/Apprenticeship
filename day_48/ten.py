import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# -----------------------------------------
# Dataset
# -----------------------------------------
data = {
    "Pixel_Intensity_Mean": [8900,7200,9500,6800,10200,7000,9800,6500],
    "Texture_Score": [12,15,18,14,20,13,19,12],
    "Shape_Complexity": [40,30,45,28,50,32,48,27],
    "Tumor": [1,0,1,0,1,0,1,0]
}

df = pd.DataFrame(data)

X = df[["Pixel_Intensity_Mean","Texture_Score","Shape_Complexity"]]
y = df["Tumor"]

# -----------------------------------------
# Train-test split
# -----------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -----------------------------------------
# Scale features
# -----------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------------------
# Train KNN
# -----------------------------------------
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Accuracy
print("Training Accuracy:", knn.score(X_train_scaled, y_train))
print("Test Accuracy:", knn.score(X_test_scaled, y_test))

# -----------------------------------------
# Predict new MRI scan
# -----------------------------------------
new_scan = pd.DataFrame([{
    "Pixel_Intensity_Mean": 9000,
    "Texture_Score": 17,
    "Shape_Complexity": 42
}])

new_scaled = scaler.transform(new_scan)
prediction = knn.predict(new_scaled)[0]

print("\nTumor Prediction for new MRI scan:", prediction)

# -----------------------------------------
# Optional: Plot scaled features
# -----------------------------------------
plt.scatter(X_train_scaled[:,0], X_train_scaled[:,1], c=y_train)
plt.title("MRI Scan Features (Scaled)")
plt.xlabel("Pixel Intensity (scaled)")
plt.ylabel("Texture Score (scaled)")
plt.show()
