# 10) Predict default of utility bill payment from overdue_days and prior_defaults
# Description: binary logistic regression model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'overdue_days':    [0, 5, 10, 2, 7, 1, 15, 3, 8, 0],
    'prior_defaults':  [0, 1, 2, 0, 1, 0, 3, 0, 1, 0],
    'default':         [0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Split features and target
X = df[['overdue_days', 'prior_defaults']]
y = df['default']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Predict for new users
new_data = pd.DataFrame({
    'overdue_days': [4, 9, 0],
    'prior_defaults': [0, 2, 0]
})

predictions = model.predict(new_data)

print("\nPredicted defaults (1=Default, 0=No Default):")
print(predictions)
