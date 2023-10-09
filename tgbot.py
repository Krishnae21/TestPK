import math

import redis
import telebot

bot = telebot.TeleBot("6612234170:AAGqKFvH0G5kyo9dVPtCmopBow9Pj_QrFo0")
r = redis.from_url("redis://redis:5470")


@bot.message_handler(content_types=["text"])
def get_factorial(message):
    try:
        msg: int = int(message.text)
        fact = r.get(str(msg))
        if fact is None:
            fact = math.factorial(msg)
            if msg >= 1000 or msg <= -1000:
                fact = str(fact)[0:5]
            r.set(str(msg), fact)
        else:
            fact.decode()
        bot.send_message(message.from_user.id, fact)
    except ValueError as ex:
        print(ex)
        bot.send_message(
            message.from_user.id, "Введите число для получения факториала."
        )


bot.polling()
