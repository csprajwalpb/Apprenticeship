# 🧠 Purchase Prediction (E-commerce)
# Metric: Gini Impurity

# ---------------------------------
# Dataset
# ---------------------------------
data = [
    {"Age": 23, "Time": 15, "Purchased": "No"},
    {"Age": 35, "Time": 45, "Purchased": "Yes"},
    {"Age": 31, "Time": 35, "Purchased": "Yes"},
    {"Age": 22, "Time": 10, "Purchased": "No"}
]

# ---------------------------------
# Gini Impurity Function
# ---------------------------------
def gini_impurity(pos, neg):
    total = pos + neg
    if total == 0:
        return 0
    p_pos = pos / total
    p_neg = neg / total
    return 1 - (p_pos ** 2 + p_neg ** 2)

# ---------------------------------
# Step 1 – Gini of entire dataset
# ---------------------------------
total_yes = sum(1 for d in data if d["Purchased"] == "Yes")
total_no  = sum(1 for d in data if d["Purchased"] == "No")
G_S = gini_impurity(total_yes, total_no)
print(f"Gini of full dataset (G(S)) = {G_S:.4f}\n")

# ---------------------------------
# Helper to split numerical attribute by a threshold
# ---------------------------------
def gini_gain_numeric(attribute, threshold):
    left  = [d for d in data if d[attribute] <= threshold]
    right = [d for d in data if d[attribute] >  threshold]

    def gini_subset(subset):
        pos = sum(1 for d in subset if d["Purchased"] == "Yes")
        neg = sum(1 for d in subset if d["Purchased"] == "No")
        return gini_impurity(pos, neg)

    g_left = gini_subset(left)
    g_right = gini_subset(right)

    weighted_gini = (len(left)/len(data))*g_left + (len(right)/len(data))*g_right
    gain = G_S - weighted_gini

    print(f"{attribute} <= {threshold}: Gini={g_left:.4f} ({len(left)} samples)")
    print(f"{attribute}  > {threshold}: Gini={g_right:.4f} ({len(right)} samples)")
    print(f"Information Gain (by Gini) for {attribute} split at {threshold} = {gain:.4f}\n")

    return gain

# ---------------------------------
# Step 2 – Try possible splits for Age and Time
# (midpoints between sorted values)
# ---------------------------------
def possible_splits(attribute):
    values = sorted(set(d[attribute] for d in data))
    return [(values[i] + values[i+1]) / 2 for i in range(len(values)-1)]

best_gain = 0
best_attr = None
best_thresh = None

for attr in ["Age", "Time"]:
    print(f"🔹 Evaluating attribute: {attr}")
    for t in possible_splits(attr):
        gain = gini_gain_numeric(attr, t)
        if gain > best_gain:
            best_gain, best_attr, best_thresh = gain, attr, t

print("✅ Best Split Summary:")
print(f"  Attribute = {best_attr}")
print(f"  Threshold = {best_thresh}")
print(f"  Gini Information Gain = {best_gain:.4f}")
