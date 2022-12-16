import requests
import json

# Replace YOUR_BOT_TOKEN with the actual token for your bot
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# The base URL for the Telegram API
API_URL = 'https://api.telegram.org/bot' + BOT_TOKEN

# A list of quotes by Andrew Tate
quotes = [
    "The only way to succeed is to work harder than anyone else.",
    "There are no shortcuts to success.",
    "The only way to achieve greatness is to never give up.",
    "If you want to succeed, you have to be willing to put in the hard work."
]

# A function that sends a message to a user or group on Telegram


def send_message(chat_id, text):
    data = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(API_URL + '/sendMessage', json=data)

# A function that handles incoming messages and commands


def handle_update(update):
    # Check if the update contains a message
    if 'message' in update:
        # Get the chat ID and message text
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        # Check if the message is a command
        if text.startswith('/'):
        # Split the command and its arguments
            tokens = text.split()
            command = tokens[0]
            args = tokens[1:]

            # Handle the '/topg' command
            if command == '/topg':
                # Send a random quote by Andrew Tate
                send_message(chat_id, quotes[0])

# A function that retrieves updates from the Telegram API


def get_updates():
    response = requests.get(API_URL + '/getUpdates')
    if response.status_code == 200:
        return response.json()['result']
    return []


# The main loop that handles updates and sends messages
while True:
    updates = get_updates()
    for update in updates:
        handle_update(update)
