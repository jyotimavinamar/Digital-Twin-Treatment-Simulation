import pandas as pd

df = pd.read_csv("dataset/raw_patients.csv")

patients = pd.DataFrame()
patients["patient_id"] = range(1, len(df) + 1)
patients["age"] = df["Age"]
patients["bmi"] = df["BMI"]
patients["glucose"] = df["Glucose"]
patients["blood_pressure"] = df["BloodPressure"]
patients["diabetes"] = df["Outcome"]

patients.to_csv("patients.csv", index=False)

print("patients.csv created successfully")
