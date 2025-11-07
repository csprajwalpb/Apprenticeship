# 8) Predict ad click from ctr_history and time_of_day_hour
# Description: whether user clicked an ad (1) from historical ctr (%) and hour bucket

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'ctr_pct': [0.5, 1.2, 0.8, 2.0, 0.3, 1.5, 0.7, 1.8, 0.4, 2.2],
    'hour': [9, 10, 14, 20, 8, 11, 16, 12, 7, 19],
    'clicked': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Split features and target
X = df[['ctr_pct', 'hour']]
y = df['clicked']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Predict for new data
new_data = pd.DataFrame({'ctr_pct': [1.0, 2.1], 'hour': [9, 18]})
predictions = model.predict(new_data)

print("\nPredicted click (1=yes, 0=no):")
print(predictions)
