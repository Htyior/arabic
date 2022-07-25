from telegram import *
from telegram.ext import *

from ..DataBase.database_handler import database

data = database()

class btn():
    def __init__(self) -> None:
        pass


    """Buttons for question games"""
    def question_btn(update: Update, context: CallbackContext):

            # send the button to user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= data.get_user_id(update, context), 
            reply_markup=ReplyKeyboardMarkup(data.question_button(update, context),
            one_time_keyboard=True)
            )

    def main_btn(update: Update, context: CallbackContext):
        
        # creating the button
        button = [["سوال بعدی"]]

        # send the button to user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"🔹گزینه مورد نظر خود را انتخاب کنید🔹",
            reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True)
            )
    
    def start_quiz(update: Update, context: CallbackContext):
        # creating the button
        button = [["شروع"]]

        # send the button to user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"""برای شروع آزمون روی گزینه شروع کلیک کن.😉""",
            reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True)
            )

    def result(update: Update, context: CallbackContext):
        # creating the button
        button = [["result"]]

        # send the button to user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello Habibi",
            reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True)
            )
