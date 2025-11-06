import pandas as pd

# 1️⃣ Create the dataset
data = {
    'years_exp': [0.5, 1, 2, 3, 4, 5, 6, 7, 8, 10],
    'salary_k': [18, 22, 28, 35, 42, 50, 58, 65, 75, 90]
}

df = pd.DataFrame(data)

# 2️⃣ Compute means
x_mean = df['years_exp'].mean()
y_mean = df['salary_k'].mean()

# 3️⃣ Compute slope (β1)
numerator = ((df['years_exp'] - x_mean) * (df['salary_k'] - y_mean)).sum()
denominator = ((df['years_exp'] - x_mean) ** 2).sum()
beta1 = numerator / denominator

# 4️⃣ Compute intercept (β0)
beta0 = y_mean - beta1 * x_mean

# 5️⃣ Predictions and residuals
df['predicted'] = beta0 + beta1 * df['years_exp']
df['residual'] = df['salary_k'] - df['predicted']

# 6️⃣ R² calculation
ss_res = (df['residual'] ** 2).sum()
ss_tot = ((df['salary_k'] - y_mean) ** 2).sum()
r2 = 1 - (ss_res / ss_tot)

# 7️⃣ Display results
print(f"Mean of X (Years of Experience): {x_mean:.2f}")
print(f"Mean of Y (Salary): {y_mean:.2f}")
print(f"Slope (β1): {beta1:.4f}")
print(f"Intercept (β0): {beta0:.4f}")
print(f"R²: {r2:.4f}\n")

print(df[['years_exp', 'salary_k', 'predicted', 'residual']])
