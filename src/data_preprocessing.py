import pandas as pd
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

def preprocess_data():
    medicines = pd.read_csv("data/medicines.csv")

    # Convert column names to lowercase to avoid case mismatch
    medicines.columns = medicines.columns.str.lower()

    if "symptoms" not in medicines.columns:
        raise KeyError("The 'symptoms' column is missing from medicines.csv. Check your CSV file!")

    stop_words = set(stopwords.words("english"))

    medicines["cleaned_symptoms"] = medicines["symptoms"].astype(str).apply(
        lambda x: " ".join([word for word in x.lower().split() if word not in stop_words])
    )

    medicines.to_csv("data/processed_medicines.csv", index=False)
    print("✅ Data Preprocessing Completed!")

if __name__ == "__main__":
    preprocess_data()
