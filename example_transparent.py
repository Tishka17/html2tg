import asyncio
import os

from aiogram import Bot
from sulguk.aiogram_middleware import SulgukMiddleware

CHAT_ID = 43022119


async def main():
    with open("example.html") as f:
        raw_html = f.read()

    raw_html="""<ol start="10">
    <li>some item</li>
    <li>other item</li>
</ol>
<p>Some <b>text</b> in a paragraph</p>"""
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    bot.session.middleware(SulgukMiddleware())
    await bot.send_message(
        chat_id=CHAT_ID,
        text=raw_html,
    )
    await bot.send_message(
        chat_id=CHAT_ID,
        text=raw_html,
        parse_mode="sulguk"
    )


asyncio.run(main())
