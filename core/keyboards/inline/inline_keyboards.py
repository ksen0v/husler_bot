from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_menu_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='⚒ Поддержка', url='tg://user?id=949735878')
    keyboard.button(text='🔗 Наш TG канал', url='https://t.me/HomeworkHustler')
    keyboard.adjust(1, 1)

    return keyboard.as_markup()