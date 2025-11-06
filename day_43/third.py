import pandas as pd

# 1️⃣ Create the dataset
data = {
    'tv_ad_k': [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5],
    'weekly_sales': [45, 50, 60, 68, 75, 82, 90, 94, 100, 106]
}

df = pd.DataFrame(data)

# 2️⃣ Compute means
x_mean = df['tv_ad_k'].mean()
y_mean = df['weekly_sales'].mean()

# 3️⃣ Compute slope (β1)
numerator = ((df['tv_ad_k'] - x_mean) * (df['weekly_sales'] - y_mean)).sum()
denominator = ((df['tv_ad_k'] - x_mean) ** 2).sum()
beta1 = numerator / denominator

# 4️⃣ Compute intercept (β0)
beta0 = y_mean - beta1 * x_mean

# 5️⃣ Predictions and residuals
df['predicted'] = beta0 + beta1 * df['tv_ad_k']
df['residual'] = df['weekly_sales'] - df['predicted']

# 6️⃣ R² calculation
ss_res = (df['residual'] ** 2).sum()
ss_tot = ((df['weekly_sales'] - y_mean) ** 2).sum()
r2 = 1 - (ss_res / ss_tot)

# 7️⃣ Display results
print(f"Mean of X (TV ad spend): {x_mean:.2f}")
print(f"Mean of Y (weekly sales): {y_mean:.2f}")
print(f"Slope (β1): {beta1:.4f}")
print(f"Intercept (β0): {beta0:.4f}")
print(f"R²: {r2:.4f}\n")

print(df[['tv_ad_k', 'weekly_sales', 'predicted', 'residual']])
