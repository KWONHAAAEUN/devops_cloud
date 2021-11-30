import pprint

import telegram
import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tasks

token = "2114338021:AAHnWg3XkYxWGSaS5Tp0pD8JkZ_ENS32QPc"
updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    """대화방이 처음 열리면 자동으로 호출"""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="안녕 나는 커비야 반가워!"
    )


def echo(update, context):
    received_text: str = update.message.text

    supported_tasks = [
        tasks.get_current_lotto_numberes,
        tasks.ya,
        tasks.naver_search,
        tasks.predict_lotto_numbers,
    ]

    for task in supported_tasks:
        if task.check_available(received_text):
            response_text = task.make_response(received_text)
            break
    else:
        response_text = "지원하지 않는 명령입니다."

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response_text)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(
    Filters.text & (~Filters.command),
    echo,
)
dispatcher.add_handler(echo_handler)
print("Started bot ...")

updater.start_polling()
updater.idle()

# bot = telegram.Bot(token)

# info = bot.getMe()
# pprint.pprint(info)

# resp = bot.getUpdates()
# pprint.pprint(resp)

# chat_id=2030049415
# bot.sendMessage(chat_id=2030049415, text="나도 그렇게 생각해 ㅋㅋ")
