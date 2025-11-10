# Loan Approval Prediction - Entropy and Information Gain Calculation

import math

# Helper function to calculate entropy
def entropy(pos, neg):
    total = pos + neg
    if total == 0:
        return 0
    p_pos = pos / total
    p_neg = neg / total
    if p_pos == 0 or p_neg == 0:
        return 0
    return - (p_pos * math.log2(p_pos) + p_neg * math.log2(p_neg))

# Dataset
data = [
    {"Income": "High", "Credit": "Good", "Loan": "Yes"},
    {"Income": "High", "Credit": "Bad", "Loan": "Yes"},
    {"Income": "Low",  "Credit": "Good", "Loan": "Yes"},
    {"Income": "Low",  "Credit": "Bad",  "Loan": "No"}
]

# Step 1: Entropy of the full dataset
total_yes = sum(1 for d in data if d["Loan"] == "Yes")
total_no  = sum(1 for d in data if d["Loan"] == "No")
E_S = entropy(total_yes, total_no)
print(f"Entropy of full set (E(S)) = {E_S:.4f}")

# Step 2: Calculate entropy for each attribute
def info_gain(attribute):
    # Find unique values of the attribute
    values = set(d[attribute] for d in data)
    weighted_entropy = 0

    for v in values:
        subset = [d for d in data if d[attribute] == v]
        pos = sum(1 for d in subset if d["Loan"] == "Yes")
        neg = sum(1 for d in subset if d["Loan"] == "No")
        E_sv = entropy(pos, neg)
        weighted_entropy += (len(subset) / len(data)) * E_sv
        print(f"  {attribute}={v}: Entropy={E_sv:.4f}")

    IG = E_S - weighted_entropy
    print(f"Information Gain for {attribute} = {IG:.4f}\n")
    return IG

# Step 3: Compute and compare
IG_income = info_gain("Income")
IG_credit = info_gain("Credit")

# Step 4: Determine best attribute
if IG_income > IG_credit:
    print("=> 'Income' is a better attribute for splitting.")
elif IG_credit > IG_income:
    print("=> 'Credit Score' is a better attribute for splitting.")
else:
    print("=> Both attributes are equally informative.")
