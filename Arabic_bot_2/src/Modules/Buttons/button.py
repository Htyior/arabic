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

    def payment(update: Update, context: CallbackContext):
        # creating the button
        button = [["میخوام پیشرفت کنم😎"]]

        # send the button to user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"""قیمت این ربات فعلا ۹۹ هزار تومن هست، که بعد از تموم شدن دوره آزمون اول(آزمونی که تو همین ربات برگذار کردیم) قیمتش بیشتر میشه.😄😄

و البته ۲۰ نفر اولی که روی دکمه پایین کلیک کنند، این ربات رو با قیمت ۷۹ هزار تومن دریافت میکنند.😍😍

پس جزو نفر های اولی باش که برای پیشرفت خودشون هزینه میکنند.😎💪🏻""",
            reply_markup=ReplyKeyboardMarkup(button, one_time_keyboard=True)
            )
