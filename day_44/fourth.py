import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create dataset
data = pd.DataFrame({
    'hours': [1.0, 2.5, 3.0, 4.0, 0.5, 5.0, 3.5, 2.0, 4.5, 1.5],
    'prior_grade': [45, 55, 60, 65, 40, 75, 62, 50, 70, 48],
    'pass': [0, 0, 1, 1, 0, 1, 1, 0, 1, 0]
})

# Split X and Y
X = data[['hours', 'prior_grade']]
y = data['pass']

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

# Predict for new students
new_data = pd.DataFrame({
    'hours': [2.0, 4.2, 5.0],
    'prior_grade': [52, 68, 80]
})
predictions = model.predict(new_data)
print("\nPredictions for new data:\n", predictions)
