import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create dataset
data = pd.DataFrame({
    'age': [25, 30, 45, 50, 35, 60, 40, 55, 48, 29],
    'bmi': [22.0, 24.5, 28.0, 31.5, 26.0, 33.0, 27.5, 30.0, 29.0, 23.5],
    'disease': [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
})

# Split X and Y
X = data[['age', 'bmi']]
y = data['disease']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Predict new cases
new_data = pd.DataFrame({
    'age': [32, 52],
    'bmi': [25.0, 30.5]
})
predictions = model.predict(new_data)
print("\nPredictions for new data:\n", predictions)
