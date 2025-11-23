"""
Django Tests for Chat Application

This module contains test cases for the chat application.
"""

from django.test import TestCase
from chat_app.chatbot_manager import get_chatbot


class ChatBotTests(TestCase):
    """
    Test cases for the ChatterBot functionality.
    """
    
    def test_chatbot_instance_creation(self):
        """
        Test that the chatbot instance is created successfully.
        """
        bot = get_chatbot()
        self.assertIsNotNone(bot)
    
    def test_chatbot_response(self):
        """
        Test that the chatbot returns a response to user input.
        """
        bot = get_chatbot()
        response = bot.get_response("Hello")
        self.assertIsNotNone(response)
        self.assertIsInstance(str(response), str)
