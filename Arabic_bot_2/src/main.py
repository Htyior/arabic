from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from Modules.Messages.message import msg
from Modules.DataBase.database_handler import database

message = msg()
data = database()

TOKEN = "5422711752:AAGnk2EEEC581GPhFXNytDtrDQhd8wJxWmo"

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
    dp.add_handler(CommandHandler("send_msg_to_all", message.send_message_to_all))
    dp.add_handler(MessageHandler(Filters.text, message.response))


    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()