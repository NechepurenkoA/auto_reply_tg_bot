from pyrogram import filters
from pyrogram.types import Message
from sqlalchemy import exists, select
from sqlalchemy.exc import IntegrityError

from src.db.database import AsyncSessionFactory
from src.db.models import TelegramUser
from src.telegram_bot.bot import Client, get_client_bot
from src.telegram_bot.templates import RESPONSE_TEMPLATE

app = get_client_bot()


@app.on_message(
    filters=filters.private,
)
async def auto_reply(client: Client, message: Message) -> None:
    async with AsyncSessionFactory() as session:
        query = select(exists().where(TelegramUser.chat_id == message.from_user.id))
        if message.from_user.id == (await app.get_me()).id or (
            await session.scalar(query)
        ):
            await session.close()
            pass
        else:
            try:
                session.add(TelegramUser(chat_id=message.from_user.id))
                await session.commit()
                await session.close()
                await app.send_message(message.chat.id, RESPONSE_TEMPLATE)
            except IntegrityError:
                pass


if __name__ == "__main__":
    app.run()
