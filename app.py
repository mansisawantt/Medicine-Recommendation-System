from flask import Flask, render_template, request
import pickle
import pandas as pd
from src.recommend import recommend_medicine

app = Flask(__name__)

# Load the trained recommendation model
with open("models/medicine_recommendation.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None
    if request.method == "POST":
        symptoms = request.form.get("symptoms")
        recommendations = recommend_medicine(symptoms, model)
    
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
