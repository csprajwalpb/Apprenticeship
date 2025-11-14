# -------------------------------------------
# 1) IMPORTS
# -------------------------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------
# 2) DATAFRAME
# -------------------------------------------
data = {
    "Glucose": [120,160,140,110,180,95,150,100],
    "BMI":     [22,30,28,24,35,20,32,23],
    "Age":     [25,45,40,30,50,22,48,27],
    "BloodPressure":[70,85,82,76,90,65,88,72],
    "Diabetes":[0,1,1,0,1,0,1,0]
}

df = pd.DataFrame(data)

X = df[["Glucose","BMI","Age","BloodPressure"]]
y = df["Diabetes"]

# -------------------------------------------
# 3) TRAIN-TEST SPLIT
# -------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# -------------------------------------------
# 4) ADD POLYNOMIAL FEATURES (Fix non-linearity)
# -------------------------------------------
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly  = poly.transform(X_test)

# -------------------------------------------
# 5) SCALE FEATURES
# -------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_poly)
X_test_scaled  = scaler.transform(X_test_poly)

# -------------------------------------------
# 6) TRAIN NON-LINEAR LOGISTIC MODEL
# -------------------------------------------
model = LogisticRegression(max_iter=500)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:,1]

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))

# -------------------------------------------
# 7) CONFUSION MATRIX
# -------------------------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap="Greens")
plt.title("Confusion Matrix (Polynomial Logistic Regression)")
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
plt.plot([0,1], [0,1], '--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid()
plt.show()
