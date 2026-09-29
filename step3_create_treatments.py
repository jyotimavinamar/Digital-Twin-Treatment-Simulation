import pandas as pd
import numpy as np

treat = pd.read_csv("dataset/raw_treatments.csv")

treatments = pd.DataFrame()
treatments["patient_id"] = range(1, len(treat) + 1)
treatments["treatment_type"] = treat["Treatment Type"]
treatments["treatment_cost"] = treat["Treatment Cost"]
treatments["hospital_days"] = treat["Hospital Stay (Days)"]
treatments["recovery_score"] = treat["Recovery Score"]

treatments.to_csv("treatments.csv", index=False)

print("treatments.csv created successfully")
