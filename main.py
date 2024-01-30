from aiogram import Bot, Dispatcher, F
import asyncio

from core.handlers.main_handlers import get_start
from core.handlers.create_order import *
from core.states.order_states import OrderInfo
from core.middlewares.get_some_photo import SomePhotoMiddleware

from texts import startup_message

TOKEN = '6408390231:AAGxAxtqolg7LsmR4QE_np_aW38UmXGUoz0'
ADMINS_ID = [949735878, 986186391]
NOTIFICATION = False


async def startup_bot(bot: Bot):
    for admin_id in ADMINS_ID:
        try:
            await bot.send_message(admin_id, startup_message)
        except:
            print(f'Не удалось отправить сообщение о запуске админу - {admin_id}')


async def main():
    bot = Bot(TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    if NOTIFICATION:
        dp.startup.register(startup_bot)

    dp.message.middleware(SomePhotoMiddleware())

    dp.message.register(get_start, F.text == '/start')
    dp.message.register(create_order, F.text.contains('💠 Создать заказ'))
    dp.message.register(get_time, OrderInfo.subject)
    dp.message.register(get_price, OrderInfo.time)
    dp.message.register(get_description, OrderInfo.price)
    dp.message.register(get_file, OrderInfo.description)
    dp.message.register(order_accepted, OrderInfo.file)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
