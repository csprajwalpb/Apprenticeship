# 🧠 Customer Churn Prediction - Using Entropy & Information Gain

import math

# Dataset
data = [
    {"Contract": "Month-to-Month", "MonthlyCharges": "High",   "Churn": "Yes"},
    {"Contract": "One Year",       "MonthlyCharges": "Low",    "Churn": "No"},
    {"Contract": "Two Year",       "MonthlyCharges": "Low",    "Churn": "No"},
    {"Contract": "Month-to-Month", "MonthlyCharges": "Medium", "Churn": "Yes"}
]

# Function to calculate entropy
def entropy(pos, neg):
    total = pos + neg
    if total == 0:
        return 0
    p_pos = pos / total
    p_neg = neg / total
    if p_pos == 0 or p_neg == 0:
        return 0
    return - (p_pos * math.log2(p_pos) + p_neg * math.log2(p_neg))

# Step 1: Entropy of full dataset
total_yes = sum(1 for d in data if d["Churn"] == "Yes")
total_no = sum(1 for d in data if d["Churn"] == "No")
E_S = entropy(total_yes, total_no)
print(f"Entropy of full set (E(S)) = {E_S:.4f}\n")

# Step 2: Function to calculate Information Gain for a given attribute
def info_gain(attribute):
    values = set(d[attribute] for d in data)
    weighted_entropy = 0

    for v in values:
        subset = [d for d in data if d[attribute] == v]
        pos = sum(1 for d in subset if d["Churn"] == "Yes")
        neg = sum(1 for d in subset if d["Churn"] == "No")
        E_sv = entropy(pos, neg)
        weighted_entropy += (len(subset) / len(data)) * E_sv
        print(f"  {attribute}={v}: Entropy={E_sv:.4f}")

    IG = E_S - weighted_entropy
    print(f"Information Gain for {attribute} = {IG:.4f}\n")
    return IG

# Step 3: Calculate Information Gain for Contract and MonthlyCharges
IG_contract = info_gain("Contract")
IG_charges  = info_gain("MonthlyCharges")

# Step 4: Determine the best attribute
if IG_contract > IG_charges:
    print("=> 'Contract' is the best attribute for the root split.")
elif IG_charges > IG_contract:
    print("=> 'MonthlyCharges' is the best attribute for the root split.")
else:
    print("=> Both attributes provide equal information gain.")
