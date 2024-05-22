"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import config
import ephem
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')
bodies_list, bodies_classes = [], []
for planet in ephem.Planet.__subclasses__():
    if planet().name is not None and planet().name not in bodies_list:
        bodies_list.append(planet().name)
        bodies_classes.append(planet)


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def planets(update, context):
    said_planet = update.message.text.split()[1].capitalize()
    dt = datetime.now().strftime('%Y/%m/%d')
    if said_planet == "List":
        update.message.reply_text(', '.join(bodies_list))
    else:
        found_body = said_planet in bodies_list
        if found_body:
            i = bodies_list.index(said_planet)
            constellation = ephem.constellation(bodies_classes[i](dt))
            update.message.reply_text(f"Constellation for {said_planet} on {dt} is {constellation[1]}")
        else:
            update.message.reply_text("Unknown planet.")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(config.api_key, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
    logging.info("Бот запущен.")


if __name__ == "__main__":
    main()
