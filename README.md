# 🤖 AI Chatbot Project

A full-stack AI chatbot with a beautiful web interface, featuring both rule-based and machine learning approaches, powered by Flask and scikit-learn.

## ✨ Features

- **Modern Web Interface**: Clean, responsive chat interface with typing indicators
- **Dual Chatbot Engines**:
  - Simple rule-based pattern matching
  - ML-powered intent classification using scikit-learn
- **RESTful API**: Flask-based backend with CORS support
- **Real-time Interaction**: Smooth chat experience with instant responses
- **Customizable Intents**: Easily extendable through intents.json

## 🚀 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Node.js (for frontend development, optional)
- Git (for version control)

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/loyojeswin/ChatBot.git
   cd ChatBot/my-chatbot
   ```

2. Set up a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r ../requirements.txt
   python -m nltk.downloader punkt wordnet omw-1.4
   ```

4. Train the ML model:
   ```bash
   python ml_chatbot.py
   ```

## 🚀 Usage

### Web Interface (Recommended)
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open `http://localhost:5000` in your browser

### API Usage
Send POST requests to `http://localhost:5000/api/chat`:

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how are you?"}'
```

Example Response:
```json
{
  "response": "Hello! How can I help you today?",
  "intent": "greeting",
  "confidence": 0.95
}
```

### Command Line Interfaces
- **ML Chatbot**: `python ml_chatbot.py`
- **Simple Chatbot**: `python simple_chatbot.py`

## 📁 Project Structure

```
my-chatbot/
├── app.py              # Flask web server and API
├── index.html          # Web interface
├── ml_chatbot.py       # ML-based chatbot
├── simple_chatbot.py   # Rule-based chatbot
├── intents.json        # Training data and responses
├── chatbot_model.pkl   # Trained ML model
├── vectorizer.pkl      # Text vectorizer
└── label_encoder.pkl   # Label encoder for intents
```

## 🛠 Customization

### Adding New Intents
1. Edit `intents.json` to add new intents, patterns, and responses
2. Retrain the ML model:
   ```bash
   python ml_chatbot.py
   ```
3. Restart the Flask server

### Styling
- Edit `index.html` to modify the chat interface
- The interface uses vanilla CSS for styling (no external dependencies)

## 🌟 Features to Add
- [ ] User authentication
- [ ] Chat history
- [ ] Support for rich media (images, buttons)
- [ ] Multi-language support

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
