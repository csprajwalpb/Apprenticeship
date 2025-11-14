import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# -----------------------------
# Dataset
# -----------------------------
data = {
    "Action": [8,6,3,2,5,4,7,3],
    "Romance": [2,1,7,8,3,4,2,6],
    "Comedy": [3,2,4,5,7,8,4,2],
    "Drama": [4,3,8,7,6,5,3,9],
    "Genre_Label": [
        "Action", "Action", "Romance", "Romance",
        "Comedy", "Comedy", "Action", "Romance"
    ]
}

df = pd.DataFrame(data)

# Encode labels
le = LabelEncoder()
df["Genre_Encoded"] = le.fit_transform(df["Genre_Label"])

# Train-test split
X = df[["Action", "Romance", "Comedy", "Drama"]]
y = df["Genre_Encoded"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# -----------------------------
# Predict for a new movie (NO WARNING)
# -----------------------------
new_movie = pd.DataFrame([{
    "Action": 6,
    "Romance": 3,
    "Comedy": 5,
    "Drama": 4
}])

pred = knn.predict(new_movie)
predicted_genre = le.inverse_transform(pred)[0]

print("\nPrediction for new movie:", predicted_genre)
