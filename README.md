# JARVIS AI Assistant

JARVIS is an advanced AI assistant for PCs, powered by Meta's LLaMA3 and Mistral AI models using Hugging Face. It leverages cutting-edge voice recognition and text-to-speech technologies to perform various tasks with simple voice commands.

## Features

- **Voice Recognition & Text-to-Speech**: Interact with JARVIS using natural voice commands.
- **Efficient ML Models**: Utilizes the most efficient models like LLaMA3 and Mistral AI for real-time data processing and web access.
- **Messaging & Calls**: Send messages or make voice/video calls with a single sentence:
  - "Send message to Srijan" followed by your message.
  - "Voice call Srijan" or "Video call Srijan".
- **Automated Apps**:
  - **WhatsApp**: Send messages with one command.
  - **YouTube**: Play videos by saying, "JARVIS, play Faded on YouTube".
  - **Notepad**: Open and edit notes with voice commands.
- **Persistent Chat History**: Stores all commands and results for the session, providing a detailed history like ChatGPT.
- **Hotword Detection**: Starts listening when you say "JARVIS", similar to "Okay Google" or "Alexa".
- **Parallel Processing**: Multi-threading for running tasks simultaneously.

## Usage

- **Start JARVIS**: Say "JARVIS" to activate the assistant.
- **Send Message**: "Send message to [Name]", followed by your message.
- **Make Calls**: "Voice call [Name]" or "Video call [Name]", for this import contacts from google in a csv format
- **Play YouTube Videos**: "JARVIS, play [Video Title] on YouTube".
- **Access Notepad**: "Open Notepad", followed by your dictation.

## Getting Started

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Srijan-D/Jarvis-AI-Assistant.git
    cd Jarvis-AI-Assistant
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Assistant**:
    ```bash
    python run.py
    ```

## Importing Google Contacts

To enable sending messages and making calls to your contacts, you need to import your Google contacts in CSV format and run the following commands in `db.py` (SQLite query):

```python
import csv
import sqlite3

# Connect to SQLite database
con = sqlite3.connect('jarvis.db')
cursor = con.cursor()

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 34th columns (1st column contains the name and 34th contains the contact number of the person)
desired_columns_indices = [0, 33]

# Read data from CSV and insert into SQLite table for the desired columns
with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        selected_data = [row[i] for i in desired_columns_indices]
        cursor.execute('''INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
con.commit()
con.close()
```

## Authenticating with Hugging Face

For authentication to Hugging Face via the `cookies.json` file, follow these steps:

1. Go to [Hugging Face Chat](https://huggingface.co/chat).
2. Use a browser extension like [Cookie-Editor](https://cookie-editor.com/) to create, edit, and delete cookies for the current tab.
3. Click on the extension after navigating to the Hugging Face Chat website and copy the cookies in JSON format.
4. Save the cookies in a `cookies.json` file as shown in the folder structure below.

## Folder Structure
Here's the folder structure for the JARVIS AI Assistant project:

JARVIS-AI-ASSISTANT/
├── engine/
│   ├── __pycache__/
│   ├── command.py
│   ├── config.py
│   ├── cookies.json (from cookie-editor)
│   ├── db.py
│   ├── features.py
│   ├── helper.py
│   ├── tempCodeRunnerFile.py
│   ├── test.py
├── frontend/
│   ├── assets/
│   ├── controller.js
│   ├── index.html
│   ├── main.js
│   ├── script.js
│   ├── style.css
├── jarvisenv/
├── .gitignore
├── contacts.csv (from google contacts)
├── jarvis.db
├── main.py
├── requirements.txt
├── run.py

## Architecture

- **Voice Recognition**: Powered by advanced NLP models from Hugging Face.
- **Text-to-Speech**: Converts AI responses into natural-sounding speech.
- **Persistent Storage**: Uses SQLite for storing chat history and commands.
- **Hotword Detection**: Always-on listening for the hotword "JARVIS".

## Example Commands

- "JARVIS, what's the weather today in Mumbai?"
- "Send message to John: I'll be late today."
- "Voice call Emily."
- "JARVIS, play the latest news on YouTube."

## Contributing
  
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue to discuss what you would like to change.


