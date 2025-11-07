# 9) Predict disease test positive from biomarker_A (single predictor)
# Description: univariate logistic regression using biomarker level

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'biomarker': [0.5, 1.2, 2.5, 3.0, 0.8, 2.0, 1.5, 2.8, 0.9, 3.2],
    'positive':  [0,   0,   1,   1,   0,   1,   0,   1,   0,   1]
}

df = pd.DataFrame(data)

# Split features and target
X = df[['biomarker']]
y = df['positive']

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

# Predict for new biomarker levels
new_data = pd.DataFrame({'biomarker': [1.0, 2.7, 3.1]})
predictions = model.predict(new_data)

print("\nPredicted test results (1=Positive, 0=Negative):")
print(predictions)
