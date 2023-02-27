import json

import dotenv
import os

import requests
from discord_webhook import DiscordWebhook

from models import Secrets, Request


def load_secrets() -> Secrets:
    dotenv.load_dotenv()
    return Secrets(
        BOT_TELEGRAM_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN"),
        BOT_DISCORD_TOKEN=os.getenv("DISCORD_BOT_TOKEN"),
        DISCORD_WEBHOOK=os.getenv("DISCORD_WEBHOOK"),
    )


def send_request(request: Request):
    params = {
        'content': "/imagine prompt:black putin"
    }

    # Send the message to the webhook URL with the specified parameters
    response = requests.post(request.discord_webhook, json=params)