# 🧠 Weather-based Play Decision - Entropy & Information Gain (ID3 Algorithm)

import math

# -------------------------------
# Dataset
# -------------------------------
data = [
    {"Outlook": "Sunny",    "Temperature": "Hot",  "Humidity": "High",   "Wind": "Weak",   "Play": "No"},
    {"Outlook": "Sunny",    "Temperature": "Hot",  "Humidity": "High",   "Wind": "Strong", "Play": "No"},
    {"Outlook": "Overcast", "Temperature": "Hot",  "Humidity": "High",   "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temperature": "Mild", "Humidity": "High",   "Wind": "Weak",   "Play": "Yes"},
    {"Outlook": "Rain",     "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak",   "Play": "Yes"}
]

# -------------------------------
# Function to calculate entropy
# -------------------------------
def entropy(pos, neg):
    total = pos + neg
    if total == 0:
        return 0
    p_pos = pos / total
    p_neg = neg / total
    if p_pos == 0 or p_neg == 0:
        return 0
    return - (p_pos * math.log2(p_pos) + p_neg * math.log2(p_neg))

# -------------------------------
# Step 1: Calculate entropy of the entire dataset
# -------------------------------
total_yes = sum(1 for d in data if d["Play"] == "Yes")
total_no  = sum(1 for d in data if d["Play"] == "No")
E_S = entropy(total_yes, total_no)
print(f"Entropy of full dataset (E(S)) = {E_S:.4f}\n")

# -------------------------------
# Step 2: Function to compute Information Gain for each feature
# -------------------------------
def info_gain(attribute):
    values = set(d[attribute] for d in data)
    weighted_entropy = 0

    for v in values:
        subset = [d for d in data if d[attribute] == v]
        pos = sum(1 for d in subset if d["Play"] == "Yes")
        neg = sum(1 for d in subset if d["Play"] == "No")
        E_sv = entropy(pos, neg)
        weighted_entropy += (len(subset) / len(data)) * E_sv
        print(f"  {attribute}={v}: Entropy={E_sv:.4f} ({len(subset)} samples)")

    IG = E_S - weighted_entropy
    print(f"Information Gain for {attribute} = {IG:.4f}\n")
    return IG

# -------------------------------
# Step 3: Compute Information Gain for all features
# -------------------------------
features = ["Outlook", "Temperature", "Humidity", "Wind"]
ig_values = {}

for f in features:
    ig_values[f] = info_gain(f)

# -------------------------------
# Step 4: Find the best attribute (Root Node)
# -------------------------------
best_feature = max(ig_values, key=ig_values.get)
print("✅ Information Gain Summary:")
for f, val in ig_values.items():
    print(f"  {f}: {val:.4f}")

print(f"\n🌳 Best feature to split (Root Node) = '{best_feature}'")
