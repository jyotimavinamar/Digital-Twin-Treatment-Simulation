import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load processed data
patients = pd.read_csv("patients.csv")
treatments = pd.read_csv("treatments.csv")

# Merge patient + treatment data
df = patients.merge(treatments, on="patient_id")

# Convert categorical treatment to numbers
df["treatment_type"] = df["treatment_type"].map({
    "Medication": 1,
    "Therapy": 2,
    "Surgery": 3
})

# Fill missing values if any
df.fillna(0, inplace=True)

# Input features
X = df[[
    "age",
    "bmi",
    "glucose",
    "blood_pressure",
    "treatment_type",
    "hospital_days"
]]

# Output (what we predict)
y = df["recovery_score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
