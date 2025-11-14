# -------------------------------------------
# 1) IMPORTS
# -------------------------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

from imblearn.over_sampling import SMOTE

# -------------------------------------------
# 2) DATAFRAME
# -------------------------------------------
data = {
    "Income": [45000,32000,78000,25000,90000,40000,50000,28000],
    "Credit_Score": [710,660,780,600,800,640,690,580],
    "Loan_Amount": [120000,80000,200000,50000,300000,70000,110000,60000],
    "Late_Payments": [0,2,0,5,0,3,1,6],
    "Default": [0,0,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

X = df[["Income","Credit_Score","Loan_Amount","Late_Payments"]]
y = df["Default"]

# -------------------------------------------
# 3) SPLIT
# -------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# -------------------------------------------
# 4) SMOTE FIX
# -------------------------------------------
smote = SMOTE(random_state=42, k_neighbors=1)   # 👈 FIX HERE
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

print("Before SMOTE:", y_train.value_counts())
print("After SMOTE:", y_train_resampled.value_counts())

# -------------------------------------------
# 5) SCALING
# -------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_resampled)
X_test_scaled  = scaler.transform(X_test)

# -------------------------------------------
# 6) MODEL
# -------------------------------------------
model = LogisticRegression()
model.fit(X_train_scaled, y_train_resampled)

y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:,1]

# -------------------------------------------
# 7) REPORTS
# -------------------------------------------
print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

# -------------------------------------------
# 8) CONFUSION MATRIX PLOT
# -------------------------------------------
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# -------------------------------------------
# 9) ROC CURVE
# -------------------------------------------
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(7,5))
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid(True)
plt.show()
