# Django ChatterBot Terminal Client

## Project Overview

This is a terminal-based conversational AI client built using Django and ChatterBot for the MSCS-633-B01 course assignment.

## Features

- Terminal-based chat interface
- Machine learning conversational responses
- Pre-trained English corpus
- Custom training data
- SQLite database storage

## Installation and Setup

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Internet connection (for downloading Spacy model during setup)

### Quick Start (Using Makefile)

```bash
# Complete setup in one command
make setup

# Start chatting
make run
```

### Manual Installation Steps

1. **Create Virtual Environment** (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
# or: make install
```

**Note:** The Spacy model is included in requirements.txt and will be installed automatically.

3. **Run Database Migrations**

```bash
python manage.py migrate
# or: make migrate
```

4. **Run the Chat Client**

```bash
python manage.py runchat
# or: make run
```

### Makefile Commands

- `make help` - Show all available commands
- `make venv` - Create virtual environment
- `make install` - Install all dependencies including Spacy model
- `make setup` - Complete setup (venv + install + migrate)
- `make run` - Start the chat client
- `make test` - Run test cases
- `make clean` - Remove cache files and database
- `make cleanall` - Remove everything including venv

## Usage

### Example Conversation

```text
user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.

user: You're welcome.
bot: Do you like hats?

user: What is your name?
bot: I am AcademicBot, a conversational AI created for academic purposes.

user: Goodbye!
bot: Goodbye! It was nice talking to you.
```

### Exit Commands

Type `quit`, `exit`, `bye`, or `goodbye` to end the conversation.

## Dependencies

- Django 5.2.8
- ChatterBot 1.2.8
- chatterbot-corpus 1.2.2
- Spacy (Natural Language Processing)
- Spacy English model (en_core_web_sm)
- SQLAlchemy 2.0
- PyYAML
- pytz
- python-dateutil

See `requirements.txt` for complete list.

**Note:** The Spacy English language model (`en_core_web_sm`) is automatically installed from requirements.txt during setup.
