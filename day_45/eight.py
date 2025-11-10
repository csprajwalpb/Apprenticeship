import math
import pandas as pd

# Dataset
data = pd.DataFrame({
    'Contains_Free': ['Yes', 'Yes', 'No', 'No'],
    'Contains_Click': ['Yes', 'No', 'Yes', 'No'],
    'Spam': ['Yes', 'Yes', 'No', 'No']
})

# Function to calculate entropy
def entropy(column):
    values = column.value_counts(normalize=True)
    return -sum(p * math.log2(p) for p in values if p > 0)

# Function to calculate information gain
def info_gain(df, attribute, target):
    total_entropy = entropy(df[target])
    values = df[attribute].unique()
    weighted_entropy = 0
    for v in values:
        subset = df[df[attribute] == v]
        weighted_entropy += (len(subset) / len(df)) * entropy(subset[target])
    return total_entropy - weighted_entropy

# Calculate target entropy
target_entropy = entropy(data['Spam'])

# Calculate IG for both attributes
ig_free = info_gain(data, 'Contains_Free', 'Spam')
ig_click = info_gain(data, 'Contains_Click', 'Spam')

# Print results
print(f"Entropy(Spam) = {target_entropy:.3f}")
print(f"Information Gain (Contains_Free) = {ig_free:.3f}")
print(f"Information Gain (Contains_Click) = {ig_click:.3f}")

# Decide the best split
best_feature = 'Contains_Free' if ig_free > ig_click else 'Contains_Click'
print(f"\n✅ Best root split: {best_feature}")
