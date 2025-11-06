import pandas as pd

# Step 1: Create the data
data = {
    'area_sqft': [850, 900, 1200, 1500, 1300, 1000, 1100, 1700, 1400, 1600],
    'price_lakhs': [35, 38, 55, 68, 60, 45, 49, 80, 66, 75]
}

df = pd.DataFrame(data)

# Step 2: Compute means
x_mean = df['area_sqft'].mean()
y_mean = df['price_lakhs'].mean()

# Step 3: Compute slope (β1)
numerator = ((df['area_sqft'] - x_mean) * (df['price_lakhs'] - y_mean)).sum()
denominator = ((df['area_sqft'] - x_mean) ** 2).sum()
beta1 = numerator / denominator

# Step 4: Compute intercept (β0)
beta0 = y_mean - beta1 * x_mean

# Step 5: Predictions ŷi
df['predicted'] = beta0 + beta1 * df['area_sqft']

# Step 6: Residuals ei
df['residual'] = df['price_lakhs'] - df['predicted']

# Step 7: R² calculation
ss_res = (df['residual'] ** 2).sum()
ss_tot = ((df['price_lakhs'] - y_mean) ** 2).sum()
r2 = 1 - (ss_res / ss_tot)

# Display results
print(f"Mean of X (area): {x_mean:.2f}")
print(f"Mean of Y (price): {y_mean:.2f}")
print(f"Slope (β1): {beta1:.4f}")
print(f"Intercept (β0): {beta0:.4f}")
print(f"R²: {r2:.4f}\n")

print(df[['area_sqft', 'price_lakhs', 'predicted', 'residual']])
