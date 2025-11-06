import pandas as pd

# 1️⃣ Create the dataset
data = {
    'session_min': [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
    'conversion_pct': [0.5, 0.8, 1.2, 1.8, 2.2, 2.5, 2.9, 3.4, 3.8, 4.0]
}

df = pd.DataFrame(data)

# 2️⃣ Compute means
x_mean = df['session_min'].mean()
y_mean = df['conversion_pct'].mean()

# 3️⃣ Compute slope (β1)
numerator = ((df['session_min'] - x_mean) * (df['conversion_pct'] - y_mean)).sum()
denominator = ((df['session_min'] - x_mean) ** 2).sum()
beta1 = numerator / denominator

# 4️⃣ Compute intercept (β0)
beta0 = y_mean - beta1 * x_mean

# 5️⃣ Predictions and residuals
df['predicted'] = beta0 + beta1 * df['session_min']
df['residual'] = df['conversion_pct'] - df['predicted']

# 6️⃣ R² calculation
ss_res = (df['residual'] ** 2).sum()
ss_tot = ((df['conversion_pct'] - y_mean) ** 2).sum()
r2 = 1 - (ss_res / ss_tot)

# 7️⃣ Display results
print(f"Mean of X (Session Duration): {x_mean:.2f}")
print(f"Mean of Y (Conversion %): {y_mean:.2f}")
print(f"Slope (β1): {beta1:.4f}")
print(f"Intercept (β0): {beta0:.4f}")
print(f"R²: {r2:.4f}\n")

print(df[['session_min', 'conversion_pct', 'predicted', 'residual']])
