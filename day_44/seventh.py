import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create dataset
data = pd.DataFrame({
    'temp_c': [45, 60, 50, 70, 55, 75, 58, 68, 52, 72],
    'vibration': [0.2, 0.8, 0.4, 1.2, 0.6, 1.5, 0.7, 1.1, 0.5, 1.3],
    'failure': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
})

# Split X and Y
X = data[['temp_c', 'vibration']]
y = data['failure']

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

# Predict for new sensor readings
new_data = pd.DataFrame({
    'temp_c': [57, 65, 75],
    'vibration': [0.6, 1.0, 1.4]
})
predictions = model.predict(new_data)
print("\nPredictions for new data:\n", predictions)
