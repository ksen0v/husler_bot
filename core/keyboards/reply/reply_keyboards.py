from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu_reply = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='💠 Создать заказ'),
    ],
    [
        KeyboardButton(text='🟢 Активные заказы'),
        KeyboardButton(text='📦 История заказов')
    ]
], resize_keyboard=True)

select_subject_reply = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Физика'),
        KeyboardButton(text='Алгебра')
    ],
    [
        KeyboardButton(text='Геометрия'),
        KeyboardButton(text='Выш. мат')
    ],
    [
        KeyboardButton(text='Информатика'),
        KeyboardButton(text='Программирование')
    ]
], resize_keyboard=True)
