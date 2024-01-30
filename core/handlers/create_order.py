from aiogram.types import Message, InputMedia, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from typing import List

from core.states.order_states import OrderInfo
from core.keyboards.reply.reply_keyboards import select_subject_reply
from texts import get_time_message, get_price_message, get_description_message, \
    create_order_message, get_photo_message, order_accepted_message


async def create_order(message: Message, state: FSMContext):
    await message.answer(create_order_message, reply_markup=select_subject_reply)
    await state.set_state(OrderInfo.subject)


async def get_time(message: Message, state: FSMContext):
    await message.answer(get_time_message.format(message.text))
    await state.update_data(data_subject=message.text)
    await state.set_state(OrderInfo.time)


async def get_price(message: Message, state: FSMContext):
    await message.answer(get_price_message.format(message.text))
    await state.update_data(data_time=message.text)
    await state.set_state(OrderInfo.price)


async def get_description(message: Message, state: FSMContext):
    await message.answer(get_description_message.format(message.text))
    await state.update_data(data_price=message.text)
    await state.set_state(OrderInfo.description)


async def get_file(message: Message, state: FSMContext):
    await message.answer(get_photo_message)
    await state.update_data(data_description=message.text)
    await state.set_state(OrderInfo.file)


async def order_accepted(message: Message, state: FSMContext, album: List[Message]):
    data = await state.get_data()
    subject = data.get('data_subject')
    time = data.get('data_time')
    price = data.get('data_price')
    description = data.get('data_description')
    order_info = order_accepted_message.format(subject, time, price, description)

    media_group = []
    for msg in album:
        if msg.photo:
            file_id = msg.photo[-1].file_id
            media_group.append(InputMediaPhoto(media=file_id))
        else:
            obj_dict = msg.Dict()
            file_id = obj_dict[msg.content_type]['file_id']
            media_group.append(InputMedia(media=file_id))

    await message.answer(order_info)
    await message.answer_media_group(media_group)
    await state.clear()
