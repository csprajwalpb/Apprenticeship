import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# ------------------------------
# STEP 1: Create Dataset
# ------------------------------
data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
    "Ad_Spend": [80000,60000,75000,90000,70000,65000,85000,95000],
    "Competitors": [3,4,3,2,4,5,3,2],
    "Seasonal_Index": [1.1,0.9,1.0,1.2,0.8,0.7,1.1,1.3],
    "Discount": [10,5,12,15,5,4,14,16],
    "Sales": [450000,320000,410000,550000,300000,280000,520000,600000]
}

df = pd.DataFrame(data)

# Features & Target
X = df[["Ad_Spend", "Competitors", "Seasonal_Index", "Discount"]]
y = df["Sales"]

# ------------------------------
# STEP 2: Train-Test Split
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.25, random_state=42
)

# ------------------------------
# STEP 3: Scaling
# ------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# ------------------------------
# STEP 4: Polynomial Features
# ------------------------------
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# ------------------------------
# STEP 5: Polynomial Regression
# ------------------------------
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_pred = poly_model.predict(X_test_poly)

print("Polynomial Regression R²:", r2_score(y_test, y_pred))


# ------------------------------
# PLOT 1: Actual vs Predicted
# ------------------------------
plt.figure(figsize=(7,5))
plt.scatter(y_test, y_pred)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)])
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.grid(True)
plt.show()


# ------------------------------
# PLOT 2: Residual Plot
# ------------------------------
residuals = y_test - y_pred

plt.figure(figsize=(7,5))
plt.scatter(y_pred, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Predicted Sales")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.grid(True)
plt.show()


# ------------------------------
# PLOT 3: Feature Importance
# Using linear regression coefficients on original features
# ------------------------------
lr = LinearRegression()
lr.fit(X, y)

importance = lr.coef_
features = X.columns

plt.figure(figsize=(7,5))
plt.bar(features, importance)
plt.title("Feature Importance (Linear Regression Coefficients)")
plt.xlabel("Features")
plt.ylabel("Coefficient Value")
plt.grid(True)
plt.show()
