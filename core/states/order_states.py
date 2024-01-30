from aiogram.fsm.state import StatesGroup, State


class OrderInfo(StatesGroup):
    subject = State()
    time = State()
    price = State()
    description = State()
    file = State()