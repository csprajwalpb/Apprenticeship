# 🧠 Student Exam Pass Prediction - Gini Impurity Calculation

# Formula:
# Gini(S) = 1 - Σ(p_i)^2

# Dataset
data = [
    {"Hours": "High",   "Attendance": "Good", "Passed": "Yes"},
    {"Hours": "Medium", "Attendance": "Good", "Passed": "Yes"},
    {"Hours": "Low",    "Attendance": "Poor", "Passed": "No"},
    {"Hours": "Low",    "Attendance": "Good", "Passed": "No"},
    {"Hours": "High",   "Attendance": "Poor", "Passed": "Yes"}
]

# Function to calculate Gini impurity
def gini_impurity(pos, neg):
    total = pos + neg
    if total == 0:
        return 0
    p_pos = pos / total
    p_neg = neg / total
    return 1 - (p_pos ** 2 + p_neg ** 2)

# Step 1: Gini of full dataset
total_yes = sum(1 for d in data if d["Passed"] == "Yes")
total_no = sum(1 for d in data if d["Passed"] == "No")
G_S = gini_impurity(total_yes, total_no)
print(f"Gini of full set (G(S)) = {G_S:.4f}\n")

# Step 2: Calculate Gini for each attribute
def gini_gain(attribute):
    values = set(d[attribute] for d in data)
    weighted_gini = 0

    for v in values:
        subset = [d for d in data if d[attribute] == v]
        pos = sum(1 for d in subset if d["Passed"] == "Yes")
        neg = sum(1 for d in subset if d["Passed"] == "No")
        G_sv = gini_impurity(pos, neg)
        weighted_gini += (len(subset) / len(data)) * G_sv
        print(f"  {attribute}={v}: Gini={G_sv:.4f}")

    gain = G_S - weighted_gini
    print(f"Information Gain (by Gini) for {attribute} = {gain:.4f}\n")
    return gain

# Step 3: Compute for both attributes
gain_hours = gini_gain("Hours")
gain_attendance = gini_gain("Attendance")

# Step 4: Determine which attribute to split first
if gain_hours > gain_attendance:
    print("=> 'Hours Studied' is a better attribute for the first split.")
elif gain_attendance > gain_hours:
    print("=> 'Attendance' is a better attribute for the first split.")
else:
    print("=> Both attributes are equally good for splitting.")
