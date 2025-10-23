# Simple Q&A Chatbot using Django and ChatterBot

This project is a simple terminal-based chatbot built with Python, Django, and ChatterBot for the course MSCS-633: Advanced Artificial Intelligence (Fall 2025).
The chatbot generates conversational responses using predefined training data and ChatterBot’s English corpus.

## Features
- Built using Django’s management command framework (terminal_bot).
- Uses ChatterBot machine-learning engine for natural conversation.
- Trained with both custom Q&A pairs and English corpus.
- Runs entirely in the terminal (no web interface required).

## Setup Instructions
1. Clone the repository
   ```bash
   clone the repository chatbot_project
   cd chatbot_project
   ```

2. Create and activate virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

4. Run migrations
   ```bash
   python manage.py migrate
   ```

5. Start the chatbot
   ```bash
   python manage.py terminal_bot
   ```

## Example Interaction
```
user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: You're welcome.
bot: Do you like hats?
```

## Project Structure
```
chatbot_project/
│
├── chatbot_app/
│   └── management/
│       └── commands/
│           └── terminal_bot.py
├── manage.py
├── requirements.txt
└── README.md
```

## Technologies Used
- Python 3.10
- Django 4.2.14
- ChatterBot 1.2.2
- spaCy 3.5.4
- SQLite (default database)
