import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create dataset
data = pd.DataFrame({
    'months_active': [2, 5, 12, 1, 8, 3, 20, 6, 4, 15],
    'last_month_spend': [120, 300, 250, 50, 180, 90, 400, 150, 80, 320],
    'churn': [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
})

# Split X and Y
X = data[['months_active', 'last_month_spend']]
y = data['churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Predict for new customers
new_data = pd.DataFrame({
    'months_active': [3, 10, 18],
    'last_month_spend': [100, 220, 380]
})
predictions = model.predict(new_data)
print("\nPredictions for new data:\n", predictions)
