import math
import pandas as pd

# Dataset
data = pd.DataFrame({
    'Fever': ['Yes', 'Yes', 'No', 'No'],
    'Cough': ['Yes', 'No', 'Yes', 'No'],
    'Flu': ['Yes', 'Yes', 'No', 'No']
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
target_entropy = entropy(data['Flu'])

# Calculate IG for each feature
ig_fever = info_gain(data, 'Fever', 'Flu')
ig_cough = info_gain(data, 'Cough', 'Flu')

# Print results
print(f"Entropy(Flu) = {target_entropy:.3f}")
print(f"Information Gain (Fever) = {ig_fever:.3f}")
print(f"Information Gain (Cough) = {ig_cough:.3f}")

# Determine best split
best_feature = 'Fever' if ig_fever > ig_cough else 'Cough'
print(f"\n✅ Best root split: {best_feature}")
