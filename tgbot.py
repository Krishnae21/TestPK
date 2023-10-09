import math

import redis
import telebot

bot = telebot.TeleBot("6612234170:AAGqKFvH0G5kyo9dVPtCmopBow9Pj_QrFo0")
r = redis.Redis(host='localhost', port=5370, db=0)


@bot.message_handler(content_types=["text"])
def get_factorial(message):
    try:
        msg: int = int(message.text)
        cache = r.get(str(msg)).decode()
        # if ():

        fact = math.factorial(msg)
        if msg >= 1000 or msg <= -1000:
            fact = str(fact)[0:5]
        r.set(str(msg), fact)

        bot.send_message(message.from_user.id, fact)
    except ValueError as ex:
        bot.send_message(
            message.from_user.id, "Введите число для получения факториала."
        )


bot.polling()
