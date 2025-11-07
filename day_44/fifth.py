import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create dataset
data = pd.DataFrame({
    'link_count': [0, 3, 1, 5, 2, 4, 0, 6, 2, 1],
    'has_attachment': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'spam': [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
})

# Split X and Y
X = data[['link_count', 'has_attachment']]
y = data['spam']

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

# Predict for new emails
new_data = pd.DataFrame({
    'link_count': [2, 5, 0],
    'has_attachment': [1, 0, 0]
})
predictions = model.predict(new_data)
print("\nPredictions for new data:\n", predictions)
