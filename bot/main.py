import os, asyncio, logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN','')
logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN) if API_TOKEN else None
dp = Dispatcher()

@dp.message(F.text.lower().startswith('/start'))
async def start(m: Message):
    await m.answer('Привет! Пришли название фильма, я найду карточку.')

@dp.message()
async def search(m: Message):
    q = m.text.strip()
    await m.answer(f'Поиск: {q}\n(Здесь будет выдача из TMDB)')

async def main():
    if not bot:
        print('Set TELEGRAM_BOT_TOKEN in env')
        return
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
