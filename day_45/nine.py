import pandas as pd

# Dataset
data = pd.DataFrame({
    'Amount': ['High', 'High', 'Low', 'Low'],
    'Foreign': ['Yes', 'No', 'No', 'Yes'],
    'Fraud': ['Yes', 'No', 'No', 'Yes']
})

# Function to calculate Gini impurity
def gini(column):
    values = column.value_counts(normalize=True)
    return 1 - sum(p ** 2 for p in values)

# Function to calculate Gini gain (similar to info gain)
def gini_gain(df, attribute, target):
    total_gini = gini(df[target])
    values = df[attribute].unique()
    weighted_gini = 0
    for v in values:
        subset = df[df[attribute] == v]
        weighted_gini += (len(subset) / len(df)) * gini(subset[target])
    return total_gini - weighted_gini

# Calculate Gini of target
target_gini = gini(data['Fraud'])

# Calculate Gini Gain for both features
gini_amount = gini_gain(data, 'Amount', 'Fraud')
gini_foreign = gini_gain(data, 'Foreign', 'Fraud')

# Print results
print(f"Gini(Fraud) = {target_gini:.3f}")
print(f"Gini Gain (Amount) = {gini_amount:.3f}")
print(f"Gini Gain (Foreign) = {gini_foreign:.3f}")

# Determine best feature
best_feature = 'Amount' if gini_amount > gini_foreign else 'Foreign'
print(f"\n✅ Best root split: {best_feature}")
