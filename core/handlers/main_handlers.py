from aiogram.types import Message
from texts import start_message
from core.keyboards.reply.reply_keyboards import start_menu_reply
from core.keyboards.inline.inline_keyboards import start_menu_inline


async def get_start(message: Message):
    await message.answer(start_message, reply_markup=start_menu_inline())
    await message.answer('👇 Главное меню 👇', reply_markup=start_menu_reply)
