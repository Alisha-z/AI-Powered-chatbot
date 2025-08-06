import re
import difflib
from datetime import datetime  # ✅ Only this is needed

# Greeting based on time
def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Dictionary of predefined rules
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "what is your name": "I'm your AI assistant.",
    "bye": "Goodbye! Have a great day.",
    "goodbye": "See you later! Take care.",
    "how are you": "I'm doing well, thank you!",
    "who made you": "I was created by a Python developer during an internship task!",
    "what can you do": "I can answer simple questions. Try saying hi or ask my name!"
}

# Clean the input
def clean_input(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Get best fuzzy match
def get_response(user_input):
    user_input = clean_input(user_input)

    if user_input in responses:
        return responses[user_input]

    # Fuzzy match
    match = difflib.get_close_matches(user_input, responses.keys(), n=1, cutoff=0.7)
    if match:
        return responses[match[0]]

    return "I'm sorry, I didn't understand that. Can you rephrase?"

# Log conversation
def log_conversation(user, bot):
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"User: {user}\nBot: {bot}\n")

# Main chatbot loop
def chat():
    print("🤖 " + get_greeting())
    print("🤖 I’m your AI assistant. Type 'exit' or 'quit' to end the chat.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("🤖 Goodbye! Have a great day!")
            break

        bot_response = get_response(user_input)
        print(f"🤖 {bot_response}")

        log_conversation(user_input, bot_response)

# Run the chatbot
if __name__ == "__main__":
    chat()
