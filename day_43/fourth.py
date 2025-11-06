import pandas as pd

# 1️⃣ Create the dataset
data = {
    'rain_mm': [400, 450, 380, 500, 550, 420, 470, 520, 480, 530],
    'yield_q': [28, 32, 26, 36, 39, 30, 34, 37, 35, 38]
}

df = pd.DataFrame(data)

# 2️⃣ Compute means
x_mean = df['rain_mm'].mean()
y_mean = df['yield_q'].mean()

# 3️⃣ Compute slope (β1)
numerator = ((df['rain_mm'] - x_mean) * (df['yield_q'] - y_mean)).sum()
denominator = ((df['rain_mm'] - x_mean) ** 2).sum()
beta1 = numerator / denominator

# 4️⃣ Compute intercept (β0)
beta0 = y_mean - beta1 * x_mean

# 5️⃣ Predictions and residuals
df['predicted'] = beta0 + beta1 * df['rain_mm']
df['residual'] = df['yield_q'] - df['predicted']

# 6️⃣ R² calculation
ss_res = (df['residual'] ** 2).sum()
ss_tot = ((df['yield_q'] - y_mean) ** 2).sum()
r2 = 1 - (ss_res / ss_tot)

# 7️⃣ Display results
print(f"Mean of X (Rainfall): {x_mean:.2f}")
print(f"Mean of Y (Yield): {y_mean:.2f}")
print(f"Slope (β1): {beta1:.4f}")
print(f"Intercept (β0): {beta0:.4f}")
print(f"R²: {r2:.4f}\n")

print(df[['rain_mm', 'yield_q', 'predicted', 'residual']])
