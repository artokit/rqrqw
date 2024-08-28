import asyncio

from aiogram import executor, Dispatcher
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from src.utils.misc import check_admin, check_staff, win_game_check, draw_bol1, draw_bol1_notify, draw_bol2, draw_bol5, \
    draw_bol6, draw_check1, draw_check2


class AdminMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        if not check_admin(message.chat.id) and not check_staff(message.chat.id):
            raise CancelHandler()


# async def main():
#     res = draw_check2(
#         "4670 3п420 2523 2425",
#         "ven",
#         "37040",
#     )
#     with open("hui.png", "wb") as f:
#         f.write(res.read())
#
#
# asyncio.run(main())


if __name__ == "__main__":
    from src.handlers import dp
    dp.middleware.setup(AdminMiddleware())
    executor.start_polling(dp, skip_updates=True)
