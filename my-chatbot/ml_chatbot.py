import json
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle
import random

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

# Define tokenizer function (not lambda - so it can be pickled)
def custom_tokenizer(text):
    return word_tokenize(text.lower())

# Load intents
with open('intents.json') as file:
    intents_data = json.load(file)

# Prepare training data
sentences = []
labels = []

for intent in intents_data['intents']:
    for pattern in intent['patterns']:
        sentences.append(pattern.lower())
        labels.append(intent['tag'])

# Vectorize text using TF-IDF with custom tokenizer
vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer)
X = vectorizer.fit_transform(sentences)

# Encode labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

# Train the model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X, y)

print("Model trained successfully!")

# Save the model and vectorizer
with open('chatbot_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

print("Model, vectorizer, and label encoder saved!")

def get_response(user_input):
    """Predict intent and return response"""
    # Vectorize user input
    input_vector = vectorizer.transform([user_input.lower()])
    
    # Predict intent
    predicted_label = model.predict(input_vector)[0]
    confidence = np.max(model.predict_proba(input_vector))
    
    # Get intent tag
    intent_tag = label_encoder.inverse_transform([predicted_label])[0]
    
    print(f"[Debug] Intent: {intent_tag}, Confidence: {confidence:.2f}")
    
    # Return response if confidence is high
    if confidence > 0.5:
        for intent in intents_data['intents']:
            if intent['tag'] == intent_tag:
                return random.choice(intent['responses'])
    
    return "I'm not sure I understand. Can you rephrase?"

# Chat loop
def chat():
    print("=" * 60)
    print("ML Chatbot: Hello! I'm your AI assistant (ML-powered).")
    print("ML Chatbot: Type 'quit' to exit.")
    print("=" * 60)
    
    while True:
        user_input = input("\nYou: ")
        
        # if user_input.lower() in ['quit', 'exit', 'bye']:
        #     print("ML Chatbot: Goodbye!")
        #     break
        
        response = get_response(user_input)
        print(f"ML Chatbot: {response}")

if __name__ == "__main__":
    chat()
