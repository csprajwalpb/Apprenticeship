import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create dataset
data = pd.DataFrame({
    'weather_clear': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    'is_weekday': [1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    'board': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
})

# Split X and Y
X = data[['weather_clear', 'is_weekday']]
y = data['board']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Predict for new conditions
new_data = pd.DataFrame({
    'weather_clear': [1, 0, 0, 1],
    'is_weekday': [0, 0, 1, 1]
})
predictions = model.predict(new_data)
print("\nPredictions for new data:\n", predictions)
