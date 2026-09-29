from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        age = int(request.form["age"])
        bmi = float(request.form["bmi"])
        glucose = int(request.form["glucose"])
        bp = int(request.form["bp"])
        treatment = int(request.form["treatment"])
        days = int(request.form["days"])

        X = np.array([[age, bmi, glucose, bp, treatment, days]])
        score = round(model.predict(X)[0], 2)

        # simulate both treatments
        med_score = round(model.predict([[age,bmi,glucose,bp,0,days]])[0], 2)
        therapy_score = round(model.predict([[age,bmi,glucose,bp,1,days]])[0], 2)

        if score >= 70:
            color = "green"
            explanation = "Excellent recovery expected with minimal complications."
        elif score >= 40:
            color = "yellow"
            explanation = "Moderate recovery. Monitoring and follow-up advised."
        else:
            color = "red"
            explanation = "Low recovery predicted. Treatment optimization needed."

        return render_template("index.html",
                               prediction=score,
                               color=color,
                               explanation=explanation,
                               med_score=med_score,
                               therapy_score=therapy_score)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
