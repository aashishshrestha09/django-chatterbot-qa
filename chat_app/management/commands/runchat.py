"""
Django Management Command: Run Chat Client

This module defines a custom Django management command to run the terminal chat client.
It allows users to start the chatbot by running: python manage.py runchat
"""

from django.core.management.base import BaseCommand
from chat_app.terminal_client import start_chat


class Command(BaseCommand):
    """
    Django management command to run the terminal chat client.

    This command initializes and starts the ChatterBot terminal interface
    when executed via Django's management system.
    """

    # Help text displayed when running: python manage.py help runchat
    help = "Runs the ChatterBot terminal client for interactive conversations"

    def add_arguments(self, parser):
        """
        Add custom command-line arguments (if needed in future).

        Args:
            parser: ArgumentParser instance for adding arguments.
        """
        # No additional arguments needed for this command currently
        pass

    def handle(self, *args, **options):
        """
        Execute the command logic.

        This method is called when the command is run. It starts the
        terminal chat client interface.

        Args:
            *args: Variable length argument list.
            **options: Arbitrary keyword arguments.
        """
        # Display command execution message
        self.stdout.write(self.style.SUCCESS("Starting ChatterBot Terminal Client..."))

        try:
            # Start the chat client
            start_chat()

            # Display success message after chat ends
            self.stdout.write(self.style.SUCCESS("Chat session ended successfully."))
        except Exception as e:
            # Handle any errors that occur during execution
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))
            raise
