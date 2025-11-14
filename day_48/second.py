# ==========================================
# DELIVERY TIME PREDICTION - NON LINEAR MODEL
# ==========================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# ------------------------------
# 1. Dataset
# ------------------------------
data = {
    'Distance_km':[2.5,5.2,1.8,9.0,3.2,7.5,4.0,6.8],
    'Traffic_Level':[4,7,3,8,5,7,5,6],
    'Items':[3,5,2,6,3,8,4,7],
    'Weather':[0,1,0,1,0,1,1,0],
    'Delivery_Time_min':[22,46,18,69,28,55,36,48]
}

df = pd.DataFrame(data)
df

# ------------------------------
# 2. Independent & Dependent Vars
# ------------------------------
X = df[['Distance_km','Traffic_Level','Items','Weather']]
y = df['Delivery_Time_min']

# ------------------------------
# 3. Polynomial Transformation
# ------------------------------
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Scale (Very Important)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_poly)

# ------------------------------
# 4. Train-test split
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42
)

# ------------------------------
# 5. Train Polynomial Regression Model
# ------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------
# 6. Evaluate
# ------------------------------
pred = model.predict(X_test)
print("R² Score:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))

# ------------------------------
# 7. Predict for a new sample
# ------------------------------
new_data = [[4, 6, 4, 1]]

new_poly = poly.transform(new_data)
new_scaled = scaler.transform(new_poly)

predicted_time = model.predict(new_scaled)
print("\nPredicted Delivery Time:", predicted_time[0])

# =======================================
# 8. Plot: Actual vs Predicted
# =======================================
import matplotlib.pyplot as plt

plt.scatter(y_test, pred)
plt.xlabel("Actual Delivery Time (min)")
plt.ylabel("Predicted Delivery Time (min)")
plt.title("Actual vs Predicted Delivery Time")

# Add reference line (y = x)
min_val = min(y_test.min(), pred.min())
max_val = max(y_test.max(), pred.max())
plt.plot([min_val, max_val], [min_val, max_val], linestyle='--')

plt.show()

