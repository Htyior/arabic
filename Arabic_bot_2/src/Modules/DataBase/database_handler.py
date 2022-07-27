import sqlite3
from time import sleep, time
from telegram import *
from telegram.ext import *
from datetime import datetime
import os

current_path = os.getcwd()

class database:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(f"/{current_path}/Modules/DataBase/DataBase.db", check_same_thread=False)
        self.cursor = self.conn.cursor()


    """Creating the database"""
    def createDatabase(self):
        self.conn = sqlite3.connect(f"/{current_path}/Modules/DataBase/DataBase.db", check_same_thread=False)
        
        # Create table for users
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users_info(
            user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
            name char,
            last_name char,
            user_name char,
            level INTEGER,
            score str,
            id str,
            payment_check int,
            lessons_needed str,
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
            lesson TEXT
        )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS other(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            number_of_users int,
            first_twiny int
        )""")



    def botStart(self, update: Update, context: CallbackContext):
        self.first_name = update.effective_user.first_name
        self.last_name = update.effective_user.last_name
        self.user_name = update.effective_user.username
        self.id = update.effective_user.id
        now = datetime.now()
        self.time = now.strftime("%Y-%m-%d %H:%M")

        self.cursor.execute(f"SELECT user_name from users_info WHERE id = ?",(self.id,))
        result = self.cursor.fetchall()
        if str(result) == "[('"+self.user_name+"',)]":
            pass

        else:    
            self.cursor.execute(f"INSERT INTO users_info (name, last_name, user_name, level, score, id, payment_check, start_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (self.first_name, self.last_name, self.user_name, 1, 0, self.id, 0, self.time))
            self.conn.commit()

            print(f"{self.first_name} {self.last_name} started the bot.(ID: {update.effective_user.username})")


    def question(self, update: Update, context: CallbackContext):
        
        self.cursor.execute(f"SELECT level FROM users_info WHERE id == {update.effective_user.id}")
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
        self.cursor.execute(f"SELECT level FROM users_info WHERE id == {update.effective_user.id}")
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
            self.cursor.execute(f"SELECT level FROM users_info WHERE id = {update.effective_user.id}")
            result = self.cursor.fetchall()
            for row in result:
                tow = int(row[0]) + 1
                self.cursor.execute(f"UPDATE users_info set level = ({tow}) WHERE id = {update.effective_user.id}")
                self.conn.commit()
                print(f"{update.effective_user.name} right answer!")


        if condition == False:
            self.cursor.execute(f"SELECT level FROM users_info WHERE id = {update.effective_user.id}")
            result = self.cursor.fetchall()
            for row in result:                
                tow = int(row[0]) + 1
                self.cursor.execute(f"UPDATE users_info set level = ({tow}) WHERE id = {update.effective_user.id}")
                self.conn.commit()
                print(f"{update.effective_user.name} wrong answer!")




    def right_answer(self, update: Update, context: CallbackContext, condition):

        if condition == True:
            self.cursor.execute(f"SELECT level FROM users_info WHERE id == {update.effective_user.id}")
            result = self.cursor.fetchall()
            for row in result:
                self.cursor.execute(f"SELECT right_option FROM level WHERE id = {row[0]}")
                question = self.cursor.fetchall()
                for tow in question:
                    return str(tow[0])
        
        if condition == False:
            self.cursor.execute(f"SELECT level FROM users_info WHERE id == {update.effective_user.id}")
            result = self.cursor.fetchall()
            for row in result:
                level = int(row[0])
                self.cursor.execute(f"SELECT right_option FROM level WHERE id = {level}")
                question = self.cursor.fetchall()
                for tow in question:
                    return str(tow[0])


    def wrong_answers(self, update: Update, context: CallbackContext):

        self.cursor.execute(f"SELECT level FROM users_info WHERE id == {update.effective_user.id}")
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

    # score up the user
    def score_up(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT score FROM users_info WHERE id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            score = int(row[0] + 1)
            self.cursor.execute(f"UPDATE users_info SET score = {score} WHERE id = {update.effective_user.id}")
            self.conn.commit()

    # check if user finished the game or not
    def check_level(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT level FROM users_info WHERE id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            return row[0]

    # return the number of score, to calculate the result of exam
    def calc_score(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT score FROM users_info WHERE id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            return row[0]
    
    # This function will send the number of current question to question_btn function in button
    def get_user_id(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT level FROM users_info WHERE id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            return f"🔹سوال {row[0]} از 40🔹"

    # This function is for sending a message to All users
    def send_msg_to_all(self, update: Update, context: CallbackContext):
        user_id_list = []
        self.cursor.execute(f"SELECT count (user_id) FROM users_info")
        result = self.cursor.fetchall()
        for row in result:
            for i in range(row[0]):
                self.cursor.execute(f"SELECT id FROM users_info WHERE user_id == {i+1}")
                result1 = self.cursor.fetchall()
                for tow in result1:
                    user_id_list.append(tow[0])
        
            # returning the number of rows and all users chat id
            return row[0], user_id_list

    # return message for sending to all users
    def message_to_all_users(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT message FROM other WHERE id == 1")
        result = self.cursor.fetchall()
        for row in result:
            return row[0]

    # Writing the lessons that the user answered the question wrong
    def lessons(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT level FROM users_info WHERE id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:

            self.cursor.execute(f"SELECT lesson FROM level WHERE id == {row[0] - 1}")
            result1 = self.cursor.fetchall()
            for tow in result1:
            
                self.cursor.execute(f"SELECT lessons_needed FROM users_info WHERE id = {update.effective_user.id}")
                result3 = self.cursor.fetchall()
                for sow in result3:
                    lesson = str(sow[0]) + ", " + str(tow[0])
            
                    self.cursor.execute(f"UPDATE users_info SET lessons_needed = '{lesson}' WHERE id = {update.effective_user.id}")
                    self.conn.commit()

    # what lessons the user should read
    def read_lessons(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT lessons_needed FROM users_info WHERE id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            return row[0]

    def first_twiny_number(self, update: Update, context: CallbackContext):
            self.cursor.execute(f"SELECT first_twiny FROM other WHERE id == 1")
            result1 = self.cursor.fetchall()
            for tow in result1:
                return tow[0]

    def first_twiny(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT payment_check FROM users_info WHERE id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            if row[0] == 0:
                    return True
            else:
                return False


    def plus_twiny(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT first_twiny FROM other WHERE id == 1")
        result = self.cursor.fetchall()
        for row in result:
            set_users_number = row[0] + 1
            self.cursor.execute(f"UPDATE other SET first_twiny = '{set_users_number}' WHERE id = 1")
            self.conn.commit()

    def change_confition(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"UPDATE users_info SET payment_check = '1' WHERE id = {update.effective_chat.id}")
        self.conn.commit()

    def number_of_users(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT number_of_users FROM other WHERE id == 1")
        result = self.cursor.fetchall()
        for row in result:
            set_users_number = row[0] + 1
            self.cursor.execute(f"UPDATE other SET number_of_users = '{set_users_number}' WHERE id = 1")
            self.conn.commit()
            return set_users_number
    

    # Check if user exist or not
    def check_user(self, update: Update, context: CallbackContext):
        self.cursor.execute(f"SELECT user_name from users_info WHERE id = ?",(update.effective_user.id,))
        result = self.cursor.fetchall()
        if str(result) == "[('"+str(update.effective_user.username)+"',)]":
            return False
            
        else:
            return True