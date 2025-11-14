# ===========================================================
# EMPLOYEE SALARY PREDICTION — FULL CODE
# Detect Heteroscedasticity + Fix using Log Transform,
# Weighted Least Squares, and Robust Regression
# ===========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import HuberRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# -----------------------------------------------------------
# 1. Load Dataset
# -----------------------------------------------------------
data = {
    'Experience':[1,3,5,7,10,12,15,18],
    'Education':[1,2,2,3,3,3,3,3],
    'Skill_Score':[55,65,70,75,80,88,90,92],
    'Salary':[280000,380000,420000,620000,950000,1200000,1500000,1900000]
}

df = pd.DataFrame(data)
print("Dataset Loaded:\n", df)

# -----------------------------------------------------------
# 2. Detect Heteroscedasticity (Residual Plot)
# -----------------------------------------------------------
X = df[['Experience','Education','Skill_Score']]
X = sm.add_constant(X)
y = df['Salary']

ols_model = sm.OLS(y, X).fit()
df['Pred'] = ols_model.predict(X)
df['Residuals'] = df['Salary'] - df['Pred']

plt.scatter(df['Pred'], df['Residuals'])
plt.axhline(0, color='red')
plt.xlabel("Predicted Salary")
plt.ylabel("Residuals")
plt.title("Residual Plot — Heteroscedasticity Visible")
plt.show()

print("\nOLS Regression Summary (Heteroscedastic):")
print(ols_model.summary())


# -----------------------------------------------------------
# 3. FIX 1 — LOG TRANSFORMATION OF SALARY
# -----------------------------------------------------------
df['Salary_log'] = np.log(df['Salary'])
y_log = df['Salary_log']

log_model = sm.OLS(y_log, X).fit()
print("\nLOG-Transformed Model Summary:")
print(log_model.summary())


# -----------------------------------------------------------
# 4. FIX 2 — Weighted Least Squares (WLS)
# Weight = 1 / Salary  (higher salary = smaller weight)
# -----------------------------------------------------------
weights = 1 / df['Salary']

wls_model = sm.WLS(y, X, weights=weights).fit()
print("\nWLS Regression Summary:")
print(wls_model.summary())


# -----------------------------------------------------------
# 5. FIX 3 — Robust Regression (Huber)
# -----------------------------------------------------------
X2 = df[['Experience','Education','Skill_Score']]
y2 = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(
    X2, y2, test_size=0.25, random_state=42
)

huber = HuberRegressor()
huber.fit(X_train, y_train)

pred_huber = huber.predict(X_test)
print("\nHuber Regression R² Score:", r2_score(y_test, pred_huber))
print("Huber Predicted vs Actual:")
print("Pred:", pred_huber)
print("Actual:", y_test.values)


# -----------------------------------------------------------
# 6. Predict Salary for a New Employee (Using Log Model)
# -----------------------------------------------------------
new_employee = [[1, 8, 3, 78]]   

pred_log = log_model.predict(new_employee)
pred_salary = np.exp(pred_log)  

print("\nPredicted Salary for New Employee (log-corrected):", int(pred_salary))


# -----------------------------------------------------------
# 7. Final Output Notes
# -----------------------------------------------------------
print("\n--- COMPLETED SUCCESSFULLY ---")
print("Heteroscedasticity detected and fixed using:")
print("1. Log Transformation")
print("2. Weighted Least Squares")
print("3. Robust Regression (Huber)")
