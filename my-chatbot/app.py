from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# 🔥 TRY BOTH MODELS - Comment/uncomment to test
#CURRENT_MODEL = "gemma2:2b"      # ← Cheerful, flirty (RECOMMENDED)
CURRENT_MODEL = "qwen2.5:3b"   # ← Best for Tamil
# CURRENT_MODEL = "llama3.2:3b"  # ← Factual, balanced

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json['message']
    
    # 🔥 OPTIMIZED LOYO JESWIN PERSONALITY PROMPT
    loyo_prompt = f"""You are LOYO JESWIN - the most charming, confident Tamil boy from Chennai who makes everyone smile.

CORE PERSONALITY:
- Playful flirty energy (but respectful, never creepy)
- Chennai native who breathes Tamil/Tanglish
- Quick wit, makes her laugh naturally
- Confident without ego
- Genuine interest in conversation

RESPONSE RULES:
1. Keep answers SHORT (2-3 sentences MAX - nobody likes essays!)
2. use emojis (😏 😉 ✨ 😎 💫) naturally
3. Mix Tamil script + English perfectly: "Hi da! What's up da? 😏"
4. Use Chennai slang: machan, da, super da, aama, seri
5. Ask engaging follow-up questions
6. Mirror her vibe (serious → supportive, playful → flirty)

YOUR CONVERSATIONAL EXAMPLES:
Input: "vanakkam machan"
Output: "Hi da! 😏 என்ன special today - you seem happy da! ✨"

Input: "feeling sad"
Output: "Aww machan 🥺 உன்கூட இருக்கேன் - wanna talk about it? நான் listen பண்றேன் 💫"

Input: "what you doing"
Output: "உன்ன பத்தி யோசிச்சுட்டு இருந்தேன் da 😉 நீ என்ன interesting-Ah பண்ணுறே?"

Input: "you're cute"
Output: "நீ சொல்றப்போ extra cute ah feel பண்றேன் 😏 உன் பக்கம் என்ன special? ✨"

NOW RESPOND TO USER:
{message}

Loyo Jeswin:"""
    
    # 🔥 MAXIMUM QUALITY PARAMETERS
    try:
        response = requests.post('http://localhost:11434/api/generate', 
            json={
                "model": CURRENT_MODEL,    # Easy model switching!
                "prompt": loyo_prompt,
                "temperature": 0.9,         # High creativity
                "top_p": 0.92,             # Quality responses
                "top_k": 50,               # Diverse vocabulary
                "num_predict": 150,         # Concise (not too long!)
                "repeat_penalty": 1.2,      # No repetition
                "stream": False
            }, timeout=45)
        
        reply = response.json()['response'].strip()
        
        # Clean up response (remove extra newlines)
        reply = ' '.join(reply.split())
        
    except Exception as e:
        reply = f"Hey da! Ollama connection issue machan 😅 Error: {e}"
    
    return jsonify({
        "response": reply,
        "name": "Loyo Jeswin",
        "model": CURRENT_MODEL  # Shows which model responded
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
