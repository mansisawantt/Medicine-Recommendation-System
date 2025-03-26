import pandas as pd
import pickle

def recommend_medicine(symptoms, model_data):
    model, tfidf, medicines = model_data

    symptoms_vectorized = tfidf.transform([symptoms])
    distances, indices = model.kneighbors(symptoms_vectorized)

    recommended_medicines = medicines.iloc[indices[0]]["medicine_name"].tolist()
    return recommended_medicines
