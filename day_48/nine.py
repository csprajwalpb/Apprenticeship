import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt

# ---------------------------
# Dataset (small sample)
# ---------------------------
data = {
    "Annual_Spend": [45000,30000,65000,20000,85000,25000,40000,70000],
    "Visit_Freq": [12,8,15,4,20,5,10,18],
    "Items_Per_Visit": [4,3,5,2,8,2,3,6]
}

df = pd.DataFrame(data)

# ---------------------------
# Scale data
# ---------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# ---------------------------
# Fast MiniBatch KMeans
# ---------------------------
k = 3  # number of clusters
model = MiniBatchKMeans(
    n_clusters=k,
    batch_size=500,       # processes in mini-batches
    random_state=42
)

model.fit(X_scaled)

# Cluster labels
df["Cluster"] = model.labels_
print(df)

# ---------------------------
# Predict new customer
# ---------------------------
new_customer = pd.DataFrame([{
    "Annual_Spend": 60000,
    "Visit_Freq": 14,
    "Items_Per_Visit": 4
}])

new_scaled = scaler.transform(new_customer)
pred_cluster = model.predict(new_scaled)[0]

print("\nPredicted segment for new customer:", pred_cluster)

# ---------------------------
# Plot (2D projection)
# ---------------------------
plt.scatter(X_scaled[:,0], X_scaled[:,1])
plt.title("Customer Clusters (Scaled)")
plt.xlabel("Annual_Spend")
plt.ylabel("Visit_Freq")
plt.show()
