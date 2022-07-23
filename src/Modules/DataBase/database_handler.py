from ast import Call
import sqlite3
from time import sleep
from defer import return_value
from telegram import *
from telegram.ext import *
from datetime import datetime
import os

from urllib3 import Retry

current_path = os.getcwd()

class database:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(f"{current_path}/Modules/DataBase/DataBase.db", check_same_thread=False)
        self.cursor = self.conn.cursor()


    """Creating the database"""
    def createDatabase(self):
        self.conn = sqlite3.connect(f"{current_path}/Modules/DataBase/DataBase.db", check_same_thread=False)
        
        # Create table for users
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users_info(
            user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
            name char,
            last_name char,
            user_name char,
            level INTEGER,
            score str,
            chat_id str,
            start_time str
        )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS level(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            right_option TEXT,
            wrong_answer_users TEXT
        )""")


    def botStart(self, update: Update, context: CallbackContext):
        self.first_name = update.effective_user.first_name
        self.last_name = update.effective_user.last_name
        self.user_name = update.effective_user.username
        self.chat_id = update.effective_chat.id
        now = datetime.now()
        self.time = now.strftime("%Y-%m-%d %H:%M")

        self.cursor.execute(f"SELECT user_name from users_info WHERE chat_id = ?",(self.chat_id,))
        result = self.cursor.fetchall()
        if str(result) == "[('"+self.user_name+"',)]":
            pass

        else:    
            self.cursor.execute(f"INSERT INTO users_info (name, last_name, user_name, level, score, chat_id, start_time) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (self.first_name, self.last_name, self.user_name, 1, 0, self.chat_id, self.time))
            self.conn.commit()

            print(f"{self.first_name} {self.last_name} started the bot.(ID: {update.effective_user.username})")


    def question(self, update: Update, context: CallbackContext):
        
        self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            self.cursor.execute(f"SELECT question FROM level WHERE id = ?", (row))
            question = self.cursor.fetchall()
            for tow in question:
                # check if the question with this id is exist or not
                if tow[0] == None:
                    update.message.reply_text("The game is over")
                else:
                    # send the question
                    update.message.reply_text(tow[0])
                            

    def question_button(self, update: Update, context: CallbackContext):
        sleep(0.5)
        self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            self.cursor.execute(f"SELECT question FROM level WHERE id = ?", (row))
            question = self.cursor.fetchall()
            for tow in question:
                # check if the question with this id is exist or not
                if tow[0] == None:
                    update.message.reply_text("The game is over")
                else:

                    # return the buttons
                    self.cursor.execute(f"SELECT option1, option2, option3, option4  FROM level WHERE id = ?", (row))
                    question = self.cursor.fetchall()
                    for tow in question:
                        return [
                            [tow[0]], [tow[1]],
                            [tow[2]], [tow[3]]
                            ]
                            


    def level_up(self, update: Update, context: CallbackContext, condition):

        if condition == True:
            self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id = {update.effective_user.id}")
            result = self.cursor.fetchall()
            for row in result:
                tow = int(row[0]) + 1
                self.cursor.execute(f"UPDATE users_info set level = ({tow}) WHERE chat_id = {update.effective_user.id}")
                self.conn.commit()
                print(f"{update.effective_user.name} right answer!")

        if condition == False:
            self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id = {update.effective_user.id}")
            result = self.cursor.fetchall()
            for row in result:
                # add the chat id number of person who wring answer
                self.cursor.execute(f"SELECT wrong_answer_users FROM level WHERE id = {row[0]}")
                result1 = self.cursor.fetchall()
                for jow in result1:
                    user = str(jow[0]) + ", " + str(update.effective_user.id)
                    self.cursor.execute(f"UPDATE level SET wrong_answer_users = '{user}' WHERE id = {row[0]}")
                    self.conn.commit()
                
                tow = int(row[0]) + 1
                self.cursor.execute(f"UPDATE users_info set level = ({tow}) WHERE chat_id = {update.effective_user.id}")
                self.conn.commit()
                print(f"{update.effective_user.name} wrong answer!")




    def right_answer(self, update: Update, context: CallbackContext, condition):

        if condition == True:
            self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
            result = self.cursor.fetchall()
            for row in result:
                self.cursor.execute(f"SELECT right_option FROM level WHERE id = {row[0]}")
                question = self.cursor.fetchall()
                for tow in question:
                    return str(tow[0])
        
        if condition == False:
            self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
            result = self.cursor.fetchall()
            for row in result:
                level = int(row[0])
                self.cursor.execute(f"SELECT right_option FROM level WHERE id = {level}")
                question = self.cursor.fetchall()
                for tow in question:
                    return str(tow[0])


    def wrong_answers(self, update: Update, context: CallbackContext):

        self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            level = int(row[0])
            self.cursor.execute(f"SELECT question FROM level WHERE id = ?", ([level]))
            question = self.cursor.fetchall()
            for tow in question:
                # check if the question with this id is exist or not
                if tow[0] == None:
                    pass
                else:
                    # return the buttons
                    self.cursor.execute(f"SELECT option1, option2, option3, option4  FROM level WHERE id = ?", ([level]))
                    question = self.cursor.fetchall()
                    for yow in question:

                        if yow[0] == database.right_answer(self, update, context, condition=False):
                            return [str(yow[1]), str(yow[2]), str(yow[3])]

                        if yow[1] == database.right_answer(self, update, context, condition=False):
                            return [str(yow[0]), str(yow[2]), str(yow[3])]

                        if yow[2] == database.right_answer(self, update, context, condition=False):
                            return [str(yow[0]), str(yow[1]), str(yow[3])]

                        if yow[3] == database.right_answer(self, update, context, condition=False):
                            return [str(yow[0]), str(yow[1]), str(yow[2])]

    def score_up(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT score FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            score = int(row[0] + 1)
            self.cursor.execute(f"UPDATE users_info SET score = {score} WHERE chat_id = {update.effective_user.id}")
            self.conn.commit()

    # check if user finished the game or not
    def check_level(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            return row[0]

    def calc_score(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT score FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            print(type(row(0)))
    
    # This function will send the number of current question to question_btn function in button
    def get_user_id(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            return f"🔹سوال {row[0]} از 40🔹"