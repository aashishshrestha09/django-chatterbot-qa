"""
Terminal Chat Client Interface

This module provides a terminal-based interface for chatting with the ChatterBot.
It handles user input, bot responses, and conversation flow.
"""

from .chatbot_manager import get_chatbot


class TerminalChatClient:
    """
    Terminal-based chat client for interacting with ChatterBot.

    This class provides a command-line interface for users to have
    conversations with the chatbot.
    """

    def __init__(self):
        """
        Initialize the terminal chat client.

        Sets up the chatbot instance and prepares the client for interaction.
        """
        self.bot = get_chatbot()
        self.running = False

    def display_welcome_message(self):
        """
        Display a welcome message when the chat client starts.
        """
        print("\n" + "=" * 60)
        print("  Welcome to ChatterBot Terminal Client")
        print("  MSCS-633-B01 - Django/ChatterBot Assignment")
        print("=" * 60)
        print("\nInstructions:")
        print("  - Type your messages and press Enter to chat")
        print("  - Type 'quit', 'exit', or 'bye' to end the conversation")
        print("  - The bot will respond to your messages")
        print("\n" + "=" * 60 + "\n")

    def get_user_input(self):
        """
        Get input from the user via the terminal.

        Returns:
            str: The user's input text.
        """
        try:
            user_input = input("user: ").strip()
            return user_input
        except (KeyboardInterrupt, EOFError):
            # Handle Ctrl+C or Ctrl+D gracefully
            return "quit"

    def get_bot_response(self, user_input):
        """
        Get a response from the chatbot based on user input.

        Args:
            user_input (str): The user's message.

        Returns:
            str: The bot's response.
        """
        try:
            response = self.bot.get_response(user_input)
            return str(response)
        except Exception as e:
            # Handle any errors gracefully
            return f"I apologize, but I encountered an error: {str(e)}"

    def should_exit(self, user_input):
        """
        Check if the user wants to exit the conversation.

        Args:
            user_input (str): The user's input text.

        Returns:
            bool: True if the user wants to exit, False otherwise.
        """
        exit_commands = ["quit", "exit", "bye", "goodbye", "stop"]
        return user_input.lower() in exit_commands

    def display_exit_message(self):
        """
        Display a goodbye message when the chat ends.
        """
        print("\n" + "=" * 60)
        print("  Thank you for using ChatterBot Terminal Client!")
        print("  Goodbye!")
        print("=" * 60 + "\n")

    def run(self):
        """
        Main loop for the terminal chat client.

        This method runs the chat interface, handling user input and bot responses
        until the user decides to exit.
        """
        self.running = True
        self.display_welcome_message()

        # Main conversation loop
        while self.running:
            # Get user input
            user_input = self.get_user_input()

            # Check if input is empty
            if not user_input:
                continue

            # Check if user wants to exit
            if self.should_exit(user_input):
                self.running = False
                self.display_exit_message()
                break

            # Get and display bot response
            bot_response = self.get_bot_response(user_input)
            print(f"bot: {bot_response}\n")


def start_chat():
    """
    Convenience function to start the terminal chat client.

    This function creates a new TerminalChatClient instance and starts
    the conversation loop.
    """
    client = TerminalChatClient()
    client.run()
