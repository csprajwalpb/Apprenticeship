import pandas as pd

# 1️⃣ Create the dataset
data = {
    'age': [22, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'bp_systolic': [110, 112, 118, 122, 128, 132, 136, 140, 145, 148]
}

df = pd.DataFrame(data)

# 2️⃣ Compute means
x_mean = df['age'].mean()
y_mean = df['bp_systolic'].mean()

# 3️⃣ Compute slope (β1)
numerator = ((df['age'] - x_mean) * (df['bp_systolic'] - y_mean)).sum()
denominator = ((df['age'] - x_mean) ** 2).sum()
beta1 = numerator / denominator

# 4️⃣ Compute intercept (β0)
beta0 = y_mean - beta1 * x_mean

# 5️⃣ Predictions and residuals
df['predicted'] = beta0 + beta1 * df['age']
df['residual'] = df['bp_systolic'] - df['predicted']

# 6️⃣ R² calculation
ss_res = (df['residual'] ** 2).sum()
ss_tot = ((df['bp_systolic'] - y_mean) ** 2).sum()
r2 = 1 - (ss_res / ss_tot)

# 7️⃣ Display results
print(f"Mean of X (Age): {x_mean:.2f}")
print(f"Mean of Y (BP Systolic): {y_mean:.2f}")
print(f"Slope (β1): {beta1:.4f}")
print(f"Intercept (β0): {beta0:.4f}")
print(f"R²: {r2:.4f}\n")

print(df[['age', 'bp_systolic', 'predicted', 'residual']])
