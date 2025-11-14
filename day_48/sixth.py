# -------------------------------------------
# 1) IMPORTS
# -------------------------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report, confusion_matrix, roc_curve, auc,
    precision_recall_curve
)
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------
# 2) CREATE DATAFRAME
# -------------------------------------------
data = {
    "Email_Length": [120,200,150,300,180,90,250,130],
    "Num_Links":    [3,6,2,10,4,1,9,3],
    "Num_Spam_Words":[0,5,1,8,3,0,6,1],
    "Sender_Reputation":[0.9,0.3,0.8,0.2,0.5,1.0,0.4,0.7],
    "Spam":[0,1,0,1,1,0,1,0]
}

df = pd.DataFrame(data)

X = df[["Email_Length","Num_Links","Num_Spam_Words","Sender_Reputation"]]
y = df["Spam"]

# -------------------------------------------
# 3) TRAIN-TEST SPLIT
# -------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# -------------------------------------------
# 4) SCALING
# -------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# -------------------------------------------
# 5) LOGISTIC REGRESSION (FIX IMBALANCE)
# -------------------------------------------
model = LogisticRegression(class_weight="balanced")   # 👈 helps recall
model.fit(X_train_scaled, y_train)

# Get probabilities
y_prob = model.predict_proba(X_test_scaled)[:,1]

# Default threshold 0.5
y_pred_default = (y_prob >= 0.5).astype(int)

print("=== Classification Report (Default Threshold 0.5) ===")
print(classification_report(y_test, y_pred_default))

# -------------------------------------------
# 6) CHOOSE LOWER THRESHOLD TO IMPROVE RECALL
# -------------------------------------------
threshold = 0.35     # 👈 you can tune this

y_pred_tuned = (y_prob >= threshold).astype(int)

print(f"\n=== Classification Report (Threshold = {threshold}) ===")
print(classification_report(y_test, y_pred_tuned))

cm = confusion_matrix(y_test, y_pred_tuned)

# -------------------------------------------
# 7) CONFUSION MATRIX HEATMAP
# -------------------------------------------
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap="Purples")
plt.title(f"Confusion Matrix (Threshold = {threshold})")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# -------------------------------------------
# 8) ROC CURVE
# -------------------------------------------
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(7,5))
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid()
plt.show()

# -------------------------------------------
# 9) PRECISION–RECALL CURVE
# -------------------------------------------
precision, recall, thresholds = precision_recall_curve(y_test, y_prob)

plt.figure(figsize=(7,5))
plt.plot(recall, precision)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision–Recall Curve")
plt.grid()
plt.show()
