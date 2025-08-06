# AI-Powered-chatbot


This repository contains a **Simple AI Chatbot** built using Python and NLP-based logic (scikit-learn and NLTK). It fulfills all the required and bonus criteria of **Task 4** in the AI Internship program.

---

## 🎯 Project Objective

Build a chatbot that can:
- Respond to greetings and simple queries.
- Use NLP techniques to classify user input.
- Simulate real-time conversation via terminal.
- Log conversations and use time-based greetings.

---

## 📁 Files Included

### 1. `main.py` – Basic Rule-Based Chatbot
- Implements simple responses using `if-else` logic.
- Responds to greetings, farewells, and name queries.
- Good for beginners to understand chatbot logic flow.

### 2. `chatbot.py` – Advanced NLP Chatbot
- Uses **TF-IDF** vectorizer + **MultinomialNB** classifier.
- Cleans user input (punctuation, lowercasing).
- Supports fuzzy matching for better accuracy.
- Greets user based on time (morning/evening).
- Logs full conversation to `chat_log.txt`.
- Gracefully handles unknown input.
- Trained on data from `intents.json`.

### 3. `train_model.py` – Model Training Script
- Reads from `intents.json`.
- Preprocesses data and vectorizes text.
- Trains the Naive Bayes model on sample intents.
- Saves the model and vectorizer using `joblib`.

### 4. `intents.json` – Intent Dataset
- Contains labeled intents (e.g., greeting, goodbye, name, etc.).
- Each intent includes several example patterns and a matching response.
- Easy to modify or expand by adding more intents.

## 💬 Example Interaction

User: Hello
Bot: Good evening! Hello! How can I help you today?

User: What is your name?
Bot: I'm your AI assistant.

User: How are you?
Bot: I'm doing well, thank you!

User: Bye
Bot: Goodbye! Have a great day.



---

## ⚙️ Features Summary

- ✅ Rule-based chatbot (basic version)
- ✅ NLP-based chatbot with training
- ✅ Input cleaning (lowercase, punctuation removal)
- ✅ Fuzzy matching for unmatched queries
- ✅ Time-based greeting (morning/evening)
- ✅ Logs all conversations to file
- ✅ Easily expandable via `intents.json`

---

## 📦 How to Run

1. **Install Requirements**
pip install scikit-learn nltk joblib

2. **Train the Model**
   python train_model.py


3. **Run the Chatbot**
python chatbot.py


---

## 👩‍💻 Submission Options

- Share the zipped folder with:
- `main.py`
- `train_model.py`
- `chatbot.py`
- `intents.json`
- `README.md`
- `chat_log.txt` (auto-created)

---

## 📌 Note

This chatbot runs in the terminal and is beginner-friendly, customizable, and ready for more AI/NLP enhancements.

 File Summaries
✅ 1. main.py
A basic chatbot using simple rule-based logic:

Uses if-else to match known questions like “hi”, “what’s your name”, etc.

No ML or NLP required.

Ideal for beginners or first-time chatbot implementation.

 2. chatbot.py
The main and most advanced chatbot script:

Loads a trained model (model.pkl) and vectorizer (vectorizer.pkl).

Preprocesses input (lowercase, punctuation, trimming).

Uses fuzzy matching (via difflib) to find closest matching intent.

Greets users depending on the time of day.

Logs all conversations into chat_log.txt with timestamps.

Handles unknown input gracefully by giving a fallback reply.

✅ 3. train_model.py
Training script that:

Loads and parses intents.json.

Uses TfidfVectorizer to convert text into features.

Trains a Multinomial Naive Bayes model.

Saves both the model and vectorizer using joblib for use in chatbot.py.

✅ 4. intents.json
JSON file storing user intents:

Each object contains:

tag: category of intent (e.g., greeting, goodbye)

patterns: example user inputs

responses: potential bot replies

Easily expandable to include new domains like weather, jokes, etc.

---



