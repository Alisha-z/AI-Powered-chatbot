import random
import json
import nltk
import spacy
from duckduckgo_search import DDGS
import joblib

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load trained model and vectorizer
model = joblib.load("intent_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Load intents
with open("intents.json") as f:
    intents = json.load(f)

def get_intent(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]

def get_response(intent):
    for item in intents['intents']:
        if item['tag'] == intent:
            return random.choice(item['responses'])
    return "Sorry, I don't understand."

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def search_knowledge_base(query):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=1)
        if results:
            return results[0]['body']
        return "Sorry, I couldn't find relevant information."

# Chat loop
print("SmartChatBot is online! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    # Intent prediction
    intent = get_intent(user_input)

    # Rule-based response
    if intent == "greeting" or intent == "goodbye" or intent == "thanks" or intent == "weather":
        response = get_response(intent)
    else:
        response = "Let me search that for you:\n" + search_knowledge_base(user_input)

    # Entity recognition
    entities = extract_entities(user_input)
    if entities:
        print("🔎 Recognized Entities:", entities)

    print("Bot:", response)
