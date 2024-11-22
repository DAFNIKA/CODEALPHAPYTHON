# Intents and Responses
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?"],
    "farewell": ["Goodbye! Take care!", "Bye! Have a nice day!"],
    "name": ["I'm ChatBot, your virtual assistant.", "You can call me ChatBot."],
    "thanks": ["You're welcome!", "Happy to help!"],
    "default": ["I'm sorry, I don't understand. Can you rephrase?", "I didn't quite get that. Could you try again?"],
}

# Keywords for intent recognition
keywords = {
    "greeting": ["hello", "hi", "hey"],
    "farewell": ["bye", "goodbye", "see you"],
    "name": ["your name", "who are you"],
    "thanks": ["thank you", "thanks"],
}


def identify_intent(user_input):
    """
    Identify the intent of the user's input based on keywords.
    """
    user_input = user_input.lower()
    for intent, words in keywords.items():
        if any(word in user_input for word in words):
            return intent
    return "default"


def chatbot():
    print("Hello! I am ChatBot. Type 'exit' to leave the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            break

        # Identify intent and respond
        intent = identify_intent(user_input)
        response = responses[intent]
        print(f"ChatBot: {response[0]}")  # Pick the first response from the list


# Run the chatbot
if __name__ == "__main__":
    chatbot()
