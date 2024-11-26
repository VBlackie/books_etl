import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")
SLACK_CHANNEL = "#all-data-engineering-books-pipeline"
print(f"inside script SLACK_API_TOKEN in script: {SLACK_API_TOKEN}")

client = WebClient(token=SLACK_API_TOKEN)


def send_slack_message(message):
    try:
        response = client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
        print(f"Message sent to Slack: {response['message']['text']}")
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

