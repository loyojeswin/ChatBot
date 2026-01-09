# Chatbot Project

A versatile chatbot implementation featuring both rule-based and machine learning approaches, with a simple web API interface.

## Features

- **Simple Rule-based Chatbot**: Basic pattern matching for responses
- **Machine Learning Chatbot**: Uses scikit-learn for intent classification
- **Web API**: Flask-based REST API for chatbot integration
- **Customizable Intents**: Easily extendable intents and responses

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git (for version control)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatbot-project.git
   cd chatbot-project
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   
   (Create requirements.txt if it doesn't exist with: `pip freeze > requirements.txt`)

## Usage

### Simple Chatbot
```bash
python my-chatbot/simple_chatbot.py
```

### ML-based Chatbot
First, train the model:
```bash
python my-chatbot/ml_chatbot.py
```

Then run the chat interface:
```bash
python my-chatbot/ml_chatbot.py
```

### Web API
Start the Flask server:
```bash
python my-chatbot/app.py
```

Then send POST requests to `http://localhost:5000/api/chat` with a JSON body:
```json
{
    "message": "Hello"
}
```

## Project Structure

```
my-chatbot/
├── app.py           # Flask web API
├── ml_chatbot.py    # ML-based chatbot
├── simple_chatbot.py # Rule-based chatbot
└── intents.json     # Training data and responses
```

## Customization

1. Edit `intents.json` to add or modify intents and responses
2. Retrain the ML model after making changes to the intents

## License

This project is open source and available under the [MIT License](LICENSE).
