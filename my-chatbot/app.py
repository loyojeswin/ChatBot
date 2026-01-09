from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize
import pickle
import json
import random

app = Flask(__name__)

# Load trained model
with open('chatbot_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Load intents
with open('intents.json') as file:
    intents_data = json.load(file)

@app.route('/api/chat', methods=['POST'])
def chat_api():
    """API endpoint for chatbot"""
    data = request.get_json()
    
    if 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400
    
    user_message = data['message']
    
    # Predict intent
    input_vector = vectorizer.transform([user_message.lower()])
    predicted_label = model.predict(input_vector)[0]
    confidence = float(model.predict_proba(input_vector).max())
    
    intent_tag = label_encoder.inverse_transform([predicted_label])[0]
    
    # Get response
    if confidence > 0.5:
        for intent in intents_data['intents']:
            if intent['tag'] == intent_tag:
                response = random.choice(intent['responses'])
                break
    else:
        response = "I'm not sure I understand."
    
    return jsonify({
        'response': response,
        'intent': intent_tag,
        'confidence': confidence
    })

@app.route('/')
def home():
    return "Chatbot API is running! Use POST /api/chat to interact."

if __name__ == '__main__':
    app.run(debug=True, port=5000)
