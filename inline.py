from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Ютуб', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Гугл', url='https://google.com')
urlkb.add(urlButton, urlButton2)


@dp.message_handler(commands=['links', 'ссылки'])
async def url_command(message: types.Message):
    await message.answer('Ссылки: ', reply_markup=urlkb)

executor.start_polling(dp, skip_updates=True)
