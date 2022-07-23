from telegram import *
from telegram.ext import *
import os

from Modules.Messages.message import msg
from Modules.DataBase.database_handler import database

message = msg()
data = database()

TOKEN = "2129217328:AAEaMBpxuKeIEiH1jKiv82jM_ANgdIxbd2k"

def main():
    """Start the bot."""

    print("Bot stated running ...")

    data.createDatabase()
    print("Database created ...")

    updater = Updater(
        TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", msg.welcomeMsg))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, message.response))


    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()