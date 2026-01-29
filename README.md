🤖 Loyo Jeswin AI Chatbot - Ollama Edition
A GPT-level multilingual chatbot featuring Loyo Jeswin - the smart, handsome Tamil boy from Chennai who speaks perfect Tamil + Tanglish + English. Powered by Ollama + Llama3.2 with a beautiful web interface.

✨ Features
GPT-Level Intelligence: Ollama Llama3.2 (1.2B params) - unlimited conversations

Multilingual Magic: Tamil script + Roman Tamil (Tanglish) + English

Loyo Jeswin Personality: Confident, flirty, Chennai slang (machan, da, super da)

Modern Web UI: WhatsApp-style chat interface

Cross-Platform: Windows, Linux, macOS

Zero Cost: 100% free local AI (no API keys)

🔥 Live Demo Examples
text
You: "vanakkam machan" 
Loyo: "வணக்கம் machan என்ன da?"

You: "single ah da" 
Loyo: "Single da! உன்கூட vibe match ஆகுதா check பண்ணலாமா? 😉"

You: "epdi iruke" 
Loyo: "Super da! நீ எப்படி இருக்கே machan? ✨"
🚀 Quick Start (2 Minutes)
Prerequisites
Python 3.8+

Git

Ollama (auto-downloads Llama3.2 model)

1. Get the Ollama Branch
bash
git clone -b ollama https://github.com/loyojeswin/ChatBot.git ChatBot-ollama
cd ChatBot-ollama/my-chatbot
2. Windows Setup
powershell
# Create Python environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install flask flask-cors requests

# Ollama auto-runs (check elephant tray icon)
ollama pull llama3.2:1b  # ~2GB download

# Run chatbot
python app.py
3. Linux/macOS Setup
bash
# Create Python environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask flask-cors requests

# Start Ollama (Terminal 1)
ollama serve

# Download model (Terminal 2)
ollama pull llama3.2:1b

# Run chatbot (Terminal 3)
python app.py
4. Open Chat
text
http://localhost:5000
Test: "vanakkam machan" → Loyo Jeswin responds! 🎉
📋 Detailed Platform Guides
Windows (Recommended)
text
1. Download: https://ollama.com/download/windows (Run as Admin)
2. Restart PowerShell/terminal
3. git clone -b ollama https://github.com/loyojeswin/ChatBot.git .
4. python -m venv venv && venv\Scripts\activate
5. pip install flask flask-cors requests
6. ollama pull llama3.2:1b  (elephant tray icon appears)
7. python app.py → http://localhost:5000
Linux (Ubuntu/Debian)
bash
curl -fsSL https://ollama.com/install.sh | sh
git clone -b ollama https://github.com/loyojeswin/ChatBot.git .
cd my-chatbot
python3 -m venv venv && source venv/bin/activate
pip install flask flask-cors requests
ollama serve & ollama pull llama3.2:1b & python app.py
Hardware Requirements
Platform	RAM	CPU	Storage
Windows/Linux	4GB+	Any modern	2GB model
Recommended	8GB+	i5/Ryzen 5	4GB free
llama3.2:1b	1.5GB	Perfect fit	✅
🔧 Project Structure
text
my-chatbot/
├── app.py                 # Flask + Ollama API (Loyo Jeswin brain)
├── index.html            # WhatsApp-style chat UI
├── intents.json          # Tamil/Tanglish training examples
├── requirements.txt      # Python dependencies
├── README.md            # This file!
└── screenshots/          # Demo GIFs
⚙️ Customization
Change Personality
Edit app.py line ~20:

python
loyo_prompt = f"""You are LOYO JESWIN - {NEW_PERSONALITY}.
Examples: ..."""
Different Model
Change app.py line ~35:

python
"model": "llama3.2:3b",  # Bigger model (slower)
"model": "gemma2:2b",    # Alternative model
New Languages
python
# app.py - Add to loyo_prompt:

🛠 Troubleshooting
Issue	Solution
"ollama not recognized"	Reinstall as Admin + restart terminal
Port 11434 busy	Good! Ollama auto-running (skip ollama serve)
Model download slow	Normal first time (~2GB)
Slow responses	Use llama3.2:1b (fastest)
🚀 Next Level Upgrades
bash
# Voice (Tamil accent)
pip install pyttsx3

# WhatsApp integration
pip install flask-ngrok

# Chat history
# Add SQLite DB

# Multi-model
ollama pull gemma2:2b phi3:mini
🌟 Loyo Jeswin Special Features
text
✅ Chennai slang: machan, da, super da, aama da
✅ Tamil script + Roman Tamil detection
✅ Flirty but respectful personality
✅ Remembers context (LLM magic)
✅ Works offline 100%
✅ Zero API costs forever
🤝 Contributing
Fork → ollama branch

Add new Tamil intents to intents.json

Test: python app.py

PR to loyojeswin:ollama 🎉

📄 License
MIT License - Free forever!

Made with ❤️ in Chennai for the world!

Test your Loyo Jeswin: http://localhost:5000 → "vanakkam machan" 😎