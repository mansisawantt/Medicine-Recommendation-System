import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

def train_recommendation_model():
    medicines = pd.read_csv("data/processed_medicines.csv")
    
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(medicines["cleaned_symptoms"])

    model = NearestNeighbors(n_neighbors=5, metric="cosine")
    model.fit(X)

    with open("models/medicine_recommendation.pkl", "wb") as model_file:
        pickle.dump((model, tfidf, medicines), model_file)

    print("Model Training Completed!")

if __name__ == "__main__":
    train_recommendation_model()
