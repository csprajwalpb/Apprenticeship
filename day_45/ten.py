import math
import pandas as pd

# Dataset
data = pd.DataFrame({
    'Income': ['High', 'Medium', 'High', 'Low'],
    'Age_Group': ['30-40', '20-30', '40-50', '20-30'],
    'Buy_Car': ['Yes', 'No', 'Yes', 'No']
})

# Function to calculate entropy
def entropy(column):
    values = column.value_counts(normalize=True)
    return -sum(p * math.log2(p) for p in values if p > 0)

# Function to calculate Information Gain
def info_gain(df, attribute, target):
    total_entropy = entropy(df[target])
    values = df[attribute].unique()
    weighted_entropy = 0
    for v in values:
        subset = df[df[attribute] == v]
        weighted_entropy += (len(subset)/len(df)) * entropy(subset[target])
    return total_entropy - weighted_entropy

# Calculate Entropy of target
target_entropy = entropy(data['Buy_Car'])

# Calculate Information Gain for both attributes
ig_income = info_gain(data, 'Income', 'Buy_Car')
ig_age = info_gain(data, 'Age_Group', 'Buy_Car')

# Print results
print(f"Entropy(Buy_Car) = {target_entropy:.3f}")
print(f"Information Gain (Income) = {ig_income:.3f}")
print(f"Information Gain (Age_Group) = {ig_age:.3f}")

# Determine best split
best_feature = 'Income' if ig_income > ig_age else 'Age_Group'
print(f"\n✅ Best root split: {best_feature}")
