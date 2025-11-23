"""
Django App Configuration for Chat Application

This module configures the chat_app Django application.
"""

from django.apps import AppConfig


class ChatAppConfig(AppConfig):
    """
    Configuration class for the chat application.

    This class defines the configuration for the chat_app Django application,
    including the app name and default auto field type.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "chat_app"
    verbose_name = "ChatterBot Chat Application"
