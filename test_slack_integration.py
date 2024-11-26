import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()


# Define the function to send messages
def send_slack_message(channel, message):
    slack_token = os.getenv("SLACK_API_TOKEN")  # Load the token from your .env
    client = WebClient(token=slack_token)
    try:
        # Send the message to the specified Slack channel
        response = client.chat_postMessage(channel=channel, text=message)
        print(f"Message sent to {channel}: {response}")
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")


# Test the function
if __name__ == "__main__":
    print(f"SLACK_API_TOKEN: {os.getenv('SLACK_API_TOKEN')}")
    # Replace with your Slack channel name
    slack_channel = "#all-data-engineering-books-pipeline"
    test_message = "Hello from the Slack bot! This is a test message."
    send_slack_message(channel=slack_channel, message=test_message)
