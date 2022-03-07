from typing import Union
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot
from aiogram.dispatcher import dispatcher

async def check(user_id, channel: Union[int, str]):
    bot = Bot.get_current()
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel)
    return member.is_chat_member()



categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Guruhga kirish",url="https://t.me/+yS41sUjfl-szMTc0"),
    ],
])

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Ovqat tavsiya qil'),
            KeyboardButton(text="2 ta ovqat tavsiya qil")
        ],
    ],
    resize_keyboard=True
)
