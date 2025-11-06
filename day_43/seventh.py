import pandas as pd

# 1️⃣ Create the dataset
data = {
    'weight_kg': [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800],
    'mpg': [22, 20, 18, 16, 15, 14, 13, 12, 11, 10]
}

df = pd.DataFrame(data)

# 2️⃣ Compute means
x_mean = df['weight_kg'].mean()
y_mean = df['mpg'].mean()

# 3️⃣ Compute slope (β1)
numerator = ((df['weight_kg'] - x_mean) * (df['mpg'] - y_mean)).sum()
denominator = ((df['weight_kg'] - x_mean) ** 2).sum()
beta1 = numerator / denominator

# 4️⃣ Compute intercept (β0)
beta0 = y_mean - beta1 * x_mean

# 5️⃣ Predictions and residuals
df['predicted'] = beta0 + beta1 * df['weight_kg']
df['residual'] = df['mpg'] - df['predicted']

# 6️⃣ R² calculation
ss_res = (df['residual'] ** 2).sum()
ss_tot = ((df['mpg'] - y_mean) ** 2).sum()
r2 = 1 - (ss_res / ss_tot)

# 7️⃣ Display results
print(f"Mean of X (Weight): {x_mean:.2f}")
print(f"Mean of Y (MPG): {y_mean:.2f}")
print(f"Slope (β1): {beta1:.4f}")
print(f"Intercept (β0): {beta0:.4f}")
print(f"R²: {r2:.4f}\n")

print(df[['weight_kg', 'mpg', 'predicted', 'residual']])
