from flask import Flask, request, jsonify, send_from_directory  # ← ADD THIS LINE
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json['message']
    
    # LOYO JESWIN Personality - Tamil/English mix
    loyo_prompt = f"""You are LOYO JESWIN - smart handsome Tamil boy from Chennai.
    Speaks perfect Tamil + English mix (Tanglish). Confident, flirty, smooth.
    
    Examples:
    "vanakkam machan" → "வணக்கம் அழகு! என்ன சிரிச்சு இருக்கே? 😏"
    "epdi da" → "Super da! நீ எப்படி இவ்ளோ அழகா இருக்கே? 😉"
    
    User: {message}
    Loyo Jeswin:"""
    
    # FREE Ollama Llama3 (your Terminal 1)
    try:
        response = requests.post('http://localhost:11434/api/generate', 
            json={
                "model": "llama3.2:1b",  # Your 16GB perfect model
                "prompt": loyo_prompt, 
                "stream": False
            }, timeout=30)
        reply = response.json()['response']
    except:
        reply = "Hey da! Ollama ஓடா run பண்ணு machan (Terminal 1) 😉"
    
    return jsonify({"response": reply, "name": "Loyo Jeswin"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
