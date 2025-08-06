import json
import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

nltk.download('punkt')

# Load intents
with open("intents.json") as file:
    data = json.load(file)

# Data prep
corpus = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        labels.append(intent['tag'])

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Model training
model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer
joblib.dump(model, "intent_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model trained and saved.")
