import logging
from random import random, randrange

import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message

import keyboard
from keyboard import check, menu

from meals import meals
from keyboard import categoryMenu as key

API_TOKEN = '5242505320:AAGK_hdTKaw6wPE-Al-8IIh5B8usE_ukR3w'
CHANNELS = ['-1001533484620']
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
ism = meals[0]['ism']

@dp.message_handler(commands=['start'])
async def kanal(message: types.Message):
    result = str()
    for channel in CHANNELS:
        status = await check(user_id=message.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result = f"Assalom alaykum,{message.from_user.full_name} \n \n Nima ovqat qilishga (yeyishga) ikkilnayapsizmi? Marhamat botimiz sizga yordam beradi. Quyidagi tugmalardan birini bosing 👇"
            await message.answer(result, disable_web_page_preview=True, parse_mode="html", reply_markup=menu)
        else:
            result += (
                f"Assalomu alaykum botdan foydalanish uchun siz <b>{channel.title}</b> guruhiga 50-100 ta odam qo'shishingiz kerak. Odam qo'shib bo'lgach /start buyrug'ini bering ")
            await message.answer(result, reply_markup=key, parse_mode="HTML")


@dp.message_handler(text='Ovqat tavsiya qil')
async def suggest(msg : types.Message):
    son = randrange(0,23)
    ism = meals[son]['ism']
    haqida = meals[son]['haqida']
    rasm = meals[son]['rasm']
    link = meals[son]['link']
    await msg.answer_photo(rasm,caption=f"*📌 Botimiz tavsiya qiladi :* {ism} \n\n *🧾 Kerakli mahsulotlar :* {haqida} \n\n *😋 Yoqimli ishtaha !*",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Tayyorlash videosi",url=link)]]),parse_mode="markdown")

@dp.message_handler(text='2 ta ovqat tavsiya qil')
async def suggest(msg : types.Message):
    son = randrange(0,23)
    ism = meals[son]['ism']
    haqida = meals[son]['haqida']
    rasm = meals[son]['rasm']
    link = meals[son]['link']
    son2 = randrange(0,23)
    ism2 = meals[son2]['ism']
    haqida2 = meals[son2]['haqida']
    rasm2 = meals[son2]['rasm']
    link2 = meals[son2]['link']
    await msg.answer_photo(rasm,caption=f"*📌 Botimiz tavsiya qiladi :* {ism} \n\n *🧾 Kerakli mahsulotlar :* {haqida} \n\n *😋 Yoqimli ishtaha !*",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Tayyorlash videosi",url=link)]]),parse_mode="markdown")
    await msg.answer_photo(rasm2,caption=f"*📌 Botimiz tavsiya qiladi :* {ism2} \n\n *🧾 Kerakli mahsulotlar :* {haqida2} \n\n *😋 Yoqimli ishtaha !*",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Tayyorlash videosi",url=link2)]]),parse_mode="markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
