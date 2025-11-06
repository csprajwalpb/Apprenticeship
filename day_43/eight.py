import pandas as pd

# 1️⃣ Create the dataset
data = {
    'temp_c': [5, 8, 10, 12, 15, 18, 20, 22, 25, 28],
    'consumption_kwh': [18, 16, 15, 14, 13, 12, 13, 14, 16, 18]
}

df = pd.DataFrame(data)

# 2️⃣ Compute means
x_mean = df['temp_c'].mean()
y_mean = df['consumption_kwh'].mean()

# 3️⃣ Compute slope (β1)
numerator = ((df['temp_c'] - x_mean) * (df['consumption_kwh'] - y_mean)).sum()
denominator = ((df['temp_c'] - x_mean) ** 2).sum()
beta1 = numerator / denominator

# 4️⃣ Compute intercept (β0)
beta0 = y_mean - beta1 * x_mean

# 5️⃣ Predictions and residuals
df['predicted'] = beta0 + beta1 * df['temp_c']
df['residual'] = df['consumption_kwh'] - df['predicted']

# 6️⃣ R² calculation
ss_res = (df['residual'] ** 2).sum()
ss_tot = ((df['consumption_kwh'] - y_mean) ** 2).sum()
r2 = 1 - (ss_res / ss_tot)

# 7️⃣ Display results
print(f"Mean of X (Temperature °C): {x_mean:.2f}")
print(f"Mean of Y (Consumption kWh): {y_mean:.2f}")
print(f"Slope (β1): {beta1:.4f}")
print(f"Intercept (β0): {beta0:.4f}")
print(f"R²: {r2:.4f}\n")

print(df[['temp_c', 'consumption_kwh', 'predicted', 'residual']])
