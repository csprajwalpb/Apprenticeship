import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create the dataset
data = pd.DataFrame({
    'annual_income_lakhs': [2.5, 3.0, 4.5, 1.8, 5.0, 2.0, 6.0, 3.5, 2.2, 4.0],
    'credit_score': [520, 580, 600, 480, 700, 500, 720, 610, 490, 650],
    'default': [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
})

# Split X and Y
X = data[['annual_income_lakhs', 'credit_score']]
y = data['default']

# Split train/test
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

# Predict for new data
new_data = pd.DataFrame({
    'annual_income_lakhs': [2.8, 5.5],
    'credit_score': [510, 710]
})
predictions = model.predict(new_data)
print("\nPredictions for new data:\n", predictions)
