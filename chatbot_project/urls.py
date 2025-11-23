"""
URL Configuration for chatbot_project

This module defines the URL patterns for the Django project.
It maps URL paths to their corresponding view functions.

For more information:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path

# URL patterns for the project
# Currently only includes the admin interface
urlpatterns = [
    path('admin/', admin.site.urls),
]
