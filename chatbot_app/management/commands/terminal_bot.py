from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

class Command(BaseCommand):
    help = "Run a simple terminal Q&A chatbot using ChatterBot"

    def handle(self, *args, **options):
        # Build the bot with SQLite storage
        bot = ChatBot(
            "TerminalQABot",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database_uri="sqlite:///db.sqlite3",
            logic_adapters=[
                "chatterbot.logic.BestMatch",
                "chatterbot.logic.TimeLogicAdapter",
                "chatterbot.logic.MathematicalEvaluation",
            ],
            read_only=False,
        )

        # Minimal custom Q&A anchors for assignment dialogue
        seed_pairs = [
            "Hi", "Hello! How can I help you today?",
            "Good morning! How are you doing?", "I am doing very well, thank you for asking.",
            "You're welcome.", "Do you like hats?",
            "What is this project?", "A simple terminal Q&A bot built with ChatterBot.",
            "Exit", "Type Ctrl+C to quit the chat."
        ]
        ListTrainer(bot).train(seed_pairs)

        # Light corpus for small talk
        ChatterBotCorpusTrainer(bot).train(
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations",
        )

        self.stdout.write(self.style.SUCCESS(
            "Bot ready. Type something (Ctrl+C to quit)."
        ))

        # Terminal chat loop
        try:
            while True:
                user_text = input("user: ")
                response = bot.get_response(user_text)
                print(f"bot: {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
