"""
ChatterBot Manager Module

This module handles the creation, configuration, and training of the ChatterBot instance.
It provides a singleton pattern to ensure only one bot instance is created.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os


class ChatBotManager:
    """
    Singleton manager class for ChatterBot instance.
    
    This class ensures only one instance of the chatbot is created and provides
    methods for bot initialization and training.
    """
    
    # Class variable to store the single bot instance
    _bot_instance = None
    
    @classmethod
    def get_bot(cls):
        """
        Get or create the ChatterBot instance.
        
        Returns:
            ChatBot: The singleton ChatterBot instance.
        """
        if cls._bot_instance is None:
            cls._bot_instance = cls._create_bot()
            cls._train_bot()
        return cls._bot_instance
    
    @classmethod
    def _create_bot(cls):
        """
        Create and configure a new ChatterBot instance.
        
        Returns:
            ChatBot: A newly configured ChatterBot instance.
        """
        # Create bot with SQLite storage adapter
        bot = ChatBot(
            name='AcademicBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///chatbot_database.db',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand.',
                    'maximum_similarity_threshold': 0.90
                }
            ],
            # Disable learning from conversations for consistency
            read_only=False
        )
        
        return bot
    
    @classmethod
    def _train_bot(cls):
        """
        Train the ChatterBot instance with corpus data and custom conversations.
        
        This method trains the bot using both the ChatterBot English corpus
        and custom conversational data to provide meaningful responses.
        """
        bot = cls._bot_instance
        
        # Train with English corpus data
        corpus_trainer = ChatterBotCorpusTrainer(bot)
        
        # Train with English greetings and conversations
        corpus_trainer.train(
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations"
        )
        
        # Train with custom conversations for better responses
        list_trainer = ListTrainer(bot)
        
        # Custom training data for polite conversation
        custom_conversations = [
            "Good morning! How are you doing?",
            "I am doing very well, thank you for asking.",
            "You're welcome.",
            "Do you like hats?",
            "I find hats quite interesting. They serve both practical and fashion purposes.",
            "That's true!",
            "Yes, I enjoy discussing various topics.",
            "What is your name?",
            "I am AcademicBot, a conversational AI created for academic purposes.",
            "Nice to meet you!",
            "Nice to meet you too! How can I help you today?",
            "How does machine learning work?",
            "Machine learning uses algorithms to learn from data and make predictions or decisions without being explicitly programmed.",
            "That's fascinating!",
            "Indeed! Machine learning is transforming many industries.",
            "Goodbye!",
            "Goodbye! It was nice talking to you.",
        ]
        
        list_trainer.train(custom_conversations)
        
        # Additional conversational training
        polite_conversations = [
            "Hello",
            "Hi there! How can I assist you?",
            "Thank you",
            "You're very welcome!",
            "How are you?",
            "I'm functioning well, thank you for asking!",
            "What can you do?",
            "I can have conversations with you on various topics. Feel free to ask me anything!",
        ]
        
        list_trainer.train(polite_conversations)


def get_chatbot():
    """
    Convenience function to get the ChatterBot instance.
    
    Returns:
        ChatBot: The singleton ChatterBot instance.
    """
    return ChatBotManager.get_bot()
