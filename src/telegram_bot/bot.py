import os

from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()


def get_client_bot() -> Client:
    app = Client(
        name="auto_replier", api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH")
    )
    return app
