# ==========================================
# REAL ESTATE PRICE PREDICTION (MULTI-REGRESSION)
# ==========================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error

# ------------------------------
# 1. Load Dataset
# ------------------------------
data = {
    'Size_sqft':[1800,2200,1500,2750,2000,3100,1400,2600],
    'Bedrooms':[3,3,2,4,3,4,2,4],
    'Age_yrs':[10,5,15,2,7,1,20,4],
    'Distance_km':[5.2,3.8,7.5,2.0,4.0,1.5,9.0,3.0],
    'Price':[8400000,9600000,6500000,12500000,8800000,14000000,5800000,11800000]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# ------------------------------
# 2. Features and Target
# ------------------------------
X = df[['Size_sqft','Bedrooms','Age_yrs','Distance_km']]
y = df['Price']

# ------------------------------
# 3. Feature Scaling
# ------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ------------------------------
# 4. Train-Test Split
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42
)

# ------------------------------
# 5. Train the Model
# ------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------
# 6. Evaluate Model
# ------------------------------
pred_test = model.predict(X_test)
print("\nR² Score:", r2_score(y_test, pred_test))
print("MAE:", mean_absolute_error(y_test, pred_test))

# ------------------------------
# 7. Predict Price for New House
# ------------------------------
new_house = [[2100, 3, 5, 4]]

# Scale the new input
new_house_scaled = scaler.transform(new_house)

predicted_price = model.predict(new_house_scaled)
print("\nPredicted Price for new house:", int(predicted_price[0]))

# =======================================
# 8. Plot: Actual vs Predicted Prices
# =======================================
import matplotlib.pyplot as plt

plt.scatter(y_test, pred_test, color='blue')
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices (Linear Regression)")

# Reference line (perfect prediction)
min_val = min(y_test.min(), pred_test.min())
max_val = max(y_test.max(), pred_test.max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--')

plt.show()

