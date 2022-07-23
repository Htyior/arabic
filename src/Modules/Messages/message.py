from telegram import *
from telegram.ext import *
import random
from time import sleep

from ..Buttons.button import btn
from ..DataBase.database_handler import database

button = btn
data = database()

class msg:
    def __init__(self) -> None:
        pass
    
    def welcomeMsg(update: Update, context: CallbackContext):
        update.message.reply_text("""
سلام ... 🤗
چطوری؟ 😏
من رباتی هستم که کمکت می‌کنم عربی خودت رو محک بزنی و ببینی سطح عربیت در چه حدی هست. 😲
حتی بهت میگم دقیقاً کجا ها ضعف داری و کمکت می‌کنم اون ضعف ها رو رو برطرف کنی.😦
بهت قول میدم اگه تا آخر با من همراه باشی عربیت کلی قوی تر میشه.😉😎
""")
        sleep(1)
        update.message.reply_text("😉")

        button.main_btn(update, context)
        data.botStart(update, context)

    
    def help(update: Update, conext: CallbackContext):
        update.message.reply_text("use the buttons")


    def response(self, update: Update, context: CallbackContext):
        # if user finished the exam, dont allow him to play
        
        if data.check_level(update, context) == 41: 
            update.message.reply_text("The exam is over.")
            button.result(update, context)
        
        else:
            if update.message.text == "سوال":
                button.question_btn(update, context)
                data.question(update, context)
        
            if update.message.text == data.right_answer(update, context, condition=True):
                right_messages = [
                    "✅آفرین، درست بود👌🏻✅",
                    "✅برافوووو✌️🏻✅",
                    "✅کارت درسته💪🏻✅",
                    "✅یه پا استادی برای خودت🤌🏻✅",
                    "✅نکنه یه وقت شانسی جواب بدی😜✅",
                    "✅دمت گرم✅",
                    "✅بابااااا، دست مارو هم بگیر😄✌️✅",
                    "✅آفرین✅"
                ]
                # create a random message
                right_message = random.choice(right_messages)
                update.message.reply_text(right_message)
                data.level_up(update, context, condition=True) # level up, score up
                button.main_btn(update, context)
                data.score_up(update, context)

            if update.message.text in data.wrong_answers(update, context):
                wrong_messages = [
                    "❌حواست کجاست؟❌",
                    "❌اشتباه بود❌",
                    "❌حواست رو جمع کن❌",
                    "❌اشتباه جواب دادی❌",
                    "❌حواست رو جمع کن خوشگله❌",
                    "❌حواست کجاست خوشگله؟❌"
                ]
                # create a random message
                wrong_message = random.choice(wrong_messages)
                update.message.reply_text(wrong_message)
                data.level_up(update, context, condition=False) # level up, no change on score
                button.main_btn(update, context)
        
#        if update.message.reply_text in "result":
#            print("result")