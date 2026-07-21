aiogram==3.7.0
aiohttp==3.9.5
aiofiles==23.2.1
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🎬 MediaFaza botiga xush kelibsiz!\n\n"
        "Hozircha bot qurilmoqda. Tez orada ishga tushadi."
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())