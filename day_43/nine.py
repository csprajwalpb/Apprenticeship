import pandas as pd

# 1️⃣ Create the dataset
data = {
    'delivery_days': [1, 2, 2, 3, 4, 5, 6, 7, 3, 2],
    'rating': [5, 4, 4, 3, 3, 2, 2, 1, 3, 4]
}

df = pd.DataFrame(data)

# 2️⃣ Compute means
x_mean = df['delivery_days'].mean()
y_mean = df['rating'].mean()

# 3️⃣ Compute slope (β1)
numerator = ((df['delivery_days'] - x_mean) * (df['rating'] - y_mean)).sum()
denominator = ((df['delivery_days'] - x_mean) ** 2).sum()
beta1 = numerator / denominator

# 4️⃣ Compute intercept (β0)
beta0 = y_mean - beta1 * x_mean

# 5️⃣ Predictions and residuals
df['predicted'] = beta0 + beta1 * df['delivery_days']
df['residual'] = df['rating'] - df['predicted']

# 6️⃣ R² calculation
ss_res = (df['residual'] ** 2).sum()
ss_tot = ((df['rating'] - y_mean) ** 2).sum()
r2 = 1 - (ss_res / ss_tot)

# 7️⃣ Display results
print(f"Mean of X (Delivery Days): {x_mean:.2f}")
print(f"Mean of Y (Rating): {y_mean:.2f}")
print(f"Slope (β1): {beta1:.4f}")
print(f"Intercept (β0): {beta0:.4f}")
print(f"R²: {r2:.4f}\n")

print(df[['delivery_days', 'rating', 'predicted', 'residual']])
