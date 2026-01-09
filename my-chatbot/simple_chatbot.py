import re
import random
import json

# Load intents
with open('intents.json') as file:
    data = json.load(file)

def find_intent(user_input):
    """Find matching intent for user input"""
    user_input = user_input.lower()
    
    # Check each intent
    for intent in data['intents']:
        # Check if any pattern matches user input
        for pattern in intent['patterns']:
            if pattern.lower() in user_input:
                return intent['tag']
    
    return None

def get_response(tag):
    """Get random response for the intent tag"""
    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    
    return "I'm sorry, I didn't understand that. Can you rephrase?"

def chatbot():
    """Main chatbot loop"""
    print("=" * 50)
    print("Chatbot: Hi! I'm your chatbot assistant.")
    print("Chatbot: Type 'bye' or 'exit' to quit.")
    print("=" * 50)
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower().strip() in ['bye', 'goodbye', 'exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Find intent and generate response
        intent_tag = find_intent(user_input)
        
        if intent_tag:
            response = get_response(intent_tag)
        else:
            response = "I'm sorry, I didn't understand that. Can you ask something else?"
        
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
