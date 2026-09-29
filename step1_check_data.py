import pandas as pd

patients = pd.read_csv("dataset/raw_patients.csv")
treatments = pd.read_csv("dataset/raw_treatments.csv")

print("PATIENT DATA")
print(patients.head())
print(patients.columns)

print("\nTREATMENT DATA")
print(treatments.head())
print(treatments.columns)
