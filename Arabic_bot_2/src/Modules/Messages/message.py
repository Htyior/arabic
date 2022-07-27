from telegram import *
from telegram.ext import *
import os
import random
from time import sleep
from collections import Counter


from ..Buttons.button import btn
from ..DataBase.database_handler import database

button = btn
data = database()

current_path = os.getcwd()


class msg:
    def __init__(self) -> None:
        self.last_msg_right = ""
        self.last_msg_wrong = ""

    def welcomeMsg(update: Update, context: CallbackContext):

        data.botStart(update, context)


        context.bot.send_message('@botbotte',
                                 text=f"{data.number_of_users(update, context)}. {update.effective_user.first_name} {update.effective_user.last_name}\nID: @{update.effective_user.username}")

        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

        sleep(1.5)

        update.message.reply_text(f"""مرحبا {update.effective_user.first_name} 🤗 کیفک؟ 😏

من رباتی هستم که کمکت می‌کنم عربی (لهجه لبنانی) خودت رو محک بزنی و ببینی سطح عربیت در چه حدی هست.

حتی بهت میگم 🔸دقیقاً🔸 کجاها ضعف داری.""")


        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(4)

        update.message.reply_text("""حالا قراره چطوری این کار رو انجام بدیم؟؟🤓
خیلی ساده ...

من الان یه امتحان تستی ازت میگیرم که ۱۵ دقیقه هم وقتت رو نمیگیره، این امتحان شامل خیلی از مباحث مهم میشه که حتما باید بلد باشی.

خودم آخرش بهت نمره میدم ...

و بهت میگم  روی کدوم مباحث بیشتر باید کار کنی.😎💪🏻""")

        sleep(7)

        update.message.reply_text("""‼️حواست باشه فقط یه بار بیشتر نمیتونی امتحان بدی، پس سعی کن قششششنگ تمرکز کنی‼️""")

        sleep(2)

        button.start_quiz(update, context)


# -----------------------------------------------------------------------------------------
    
    def send_message_to_all(self, update: Update, context: CallbackContext):
        if update.effective_user.id == 1331350150:
            user_id_list =  data.send_msg_to_all(update, context)
            message = data.message_to_all_users(update, context)

            for i in range(user_id_list[0]):
                context.bot.send_message(chat_id=user_id_list[1][i], text=message)

        else:
            pass


# ------------------------------------------------------------------------------------------

    def response(self, update: Update, context: CallbackContext):
        # if user finished the exam, dont allow him to play
        
        if data.check_level(update, context) == 41: 

            if update.message.text == "میخوام پیشرفت کنم😎":
                condition = data.first_twiny(update, context)
                if condition == True:
                    data.change_confition(update, context)

                    if data.first_twiny_number(update, context) <20:
                        data.plus_twiny(update, context)

                        update.message.reply_text("""به موقع رسیدی🤩
هنوز ظرفیت مونده، هزینه ای که قراره بکنی در مقابل خدمات و تجربه ای که به دست میاری هیچی نیست😊
چون خیلی ها هستند که میخوان از این ربات استفاده کنند و ما فقط به بیست نفر اجازه دادیم که از تخفیف استفاده کنند، فقط یک ساعت وقت داری که مبلغ رو واریز کنی، بعد یک ساعت ظرفیت به نفر بعدی داده میشه.💚💚
مبلغ 79 هزار تومن رو  به شماره کارتی که برات میفرستم واریز کن و فیش رو برای اکانتی که بهت میگم بفرست.😁❤️""")

                        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                        sleep(10)

                        update.message.reply_text("""💳 6037-9919-2302-2549
حسین رضایی

@THISISMREN""")


                        context.bot.send_message(chat_id="665540201",
                                             text=f'{data.first_twiny_number(update, context)}. @{update.effective_user.username}')
        
        
        
        
                    else:

                        data.plus_twiny(update, context)

                        update.message.reply_text("""ببخشید😢
یکم دیر اومدی و ظرفیت بیست نفر اول تکمیل شد🤦‍♂️
ولی اصلا ناراحت نباش، چون هزینه ای که میخوای بکنی در مقابل خدمات و تجربیاتی که به دست میاری خییلی ناچیزه، این رو هم در نظر داشته باش که قیمت این ربات رو فعلا پایین آوردیم که تو بتونی ازش استفاده کنی و پیشرفت کنی.

⚠️ این ربات دیگه با این قیمت عرضه نمیشه😁✋

مبلغ 99 هزار تومن رو  به شماره کارتی که برات میفرستم واریز کن و فیش رو برای اکانتی که بهت میگم بفرست.😁❤️""")

                        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                        sleep(10)

                        update.message.reply_text("""💳 6037-9919-2302-2549
حسین رضایی

@THISISMREN""")

                        context.bot.send_message(chat_id="665540201",
                                             text=f'{data.first_twiny_number(update, context)}. @{update.effective_user.username}')



                else:
                    pass




            else:

                update.message.reply_text("""امتحان تموم شد😁\nیک دقیقه صبر کن تا نتیجه رو محاسبه کنم و برات بفرستم😉""")
    
                sleep(5)

                score = data.calc_score(update, context)
                right = score
                wrong = 40 - right
                final = int((right / 40) * 100)

                context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

                sleep(5)

                update.message.reply_text(f"""نتیجه امتحانت آماده شد.""")

                sleep(2)

                update.message.reply_text(f"""
                ✅ تعداد جواب های درست: {right}\n\n❌تعداد جواب های غلط: {wrong}\n\n🔻نمره از 100: {final}""")

                sleep(4)

                if final == 100:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    sleep(5)
                    update.message.reply_text("""بابا کارت درسته 🤯🤯
لهجه لبنانی ت عالی هست و مشخصه می‌دونی داری چیکار می‌کنی.
سوالات از موضوعات مختلفی بود، ولی تو همش رو درست جواب دادی. این یعنی قبلا با همه این ها مواجه شدی و روشون کار کردی.😁👌
ولی حواست باشه به خودت مغرور نشی اصلااا، لحظه ای که به خودت مغرور بشی دقیقاً همون لحظه ایه که دیگه پیشرفت نمی‌کنی.
مطمئناً هنوز خیلی چیز ها هست که باید یاد بگیری.
اگه خودتم این احساس رو داری با من همراه شو
تا مطالب دیگه رو هم با هم کار کنیم""")


                if 100 > final > 70:
                    test = data.read_lessons(update, context)
                    test = test.split(", ")
                    testi = Counter(test)
                    s = "\n⚠️".join(testi.keys())
                    s = s.replace('None', '')
                    s = "🔰 این ها مواردی هست که تو درشون ضعف داری و باید بیشتر روی اون ها کار کنی:\n" + s 
                    update.message.reply_text(s)

                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    sleep(5)
                    update.message.reply_text("""✅حالا میخوام کمکت کنم جواب همه سوالاتت رو پیدا کنی و سطح عربیت رو بالاتر ببری.✅""")

                if 70 > final > 40:
                    test = data.read_lessons(update, context)
                    test = test.split(", ")
                    testi = Counter(test)
                    s = "\n⚠️".join(testi.keys())
                    s = s.replace('None', '')
                    s = "🔰 این ها مواردی هست که تو درشون ضعف داری و باید بیشتر روی اون ها کار کنی:\n" + s 
                    update.message.reply_text(s)

                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    sleep(5)
                    update.message.reply_text("""✅حالا میخوام کمکت کنم جواب همه سوالاتت رو پیدا کنی و سطح عربیت رو بالاتر ببری.✅""")


                if final < 40:
                    test = data.read_lessons(update, context)
                    test = test.split(", ")
                    testi = Counter(test)
                    s = "\n⚠️".join(testi.keys())
                    s = s.replace('None', '')
                    s = "🔰 این ها مواردی هست که تو درشون ضعف داری و باید بیشتر روی اون ها کار کنی:\n" + s 
                    update.message.reply_text(s)

                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    sleep(5)
                    update.message.reply_text("""✅حالا میخوام کمکت کنم جواب همه سوالاتت رو پیدا کنی و سطح عربیت رو بالاتر ببری.✅""")


                context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                sleep(5)


                update.message.reply_text("""🔹من واست یه مرجع لبنانی ساختم، که مادام العمر دستته و راحت میتونی به هر درسنامه ای که میخوای دسترسی داشته باشی..✌️

🔷اینا بخشی از خدمات من هست:
✅ کلمات(بر محوریت مکان و موضوع)
✅ قواعد
✅ کلیپ های کوتاه عربی همراه با متن 
✅ آهنگ های لبنانی
✅ پادکست های لبنانی

💯مهم تر از همه ...
✅ خودم کنارت هستم و تجربه های خیلی مفید خودم و بقیه کسایی که مسیر تورو خیلی وقت پیش رفتند رو در اختیارت میذارم و کمکت میکنم بتونی زودتر رشد کنی.😎😊🤗


دیگه منتظر چی هستی؟!
زودتر از بقیه پیشرفت کن💪🏻، منم کنارتم..🥳""")


                context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                sleep(10)

                button.payment(update, context)




        else:
            if update.message.text == "سوال بعدی":
                button.question_btn(update, context)
                data.question(update, context)

            if update.message.text == "شروع":
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
                    "✅آفرین✅",
                    "✅آفرین . واسه سوال بعدی آماده ای؟✅",
                    "✅عالیه . همینطوری ادامه بده✅",
                    "✅احسنت . اینم که درست جواب دادی، ببینم تا آخر چیکار میکنی!✅",
                    "✅ممتاز . داری عالی پیش میری✅",
                    "✅دمت گرم🤗✅",
                    "✅کارت عالیه، با همین فرمون برو جلو🤓✅",
                    "✅داری عالی پیش میری😇✅",
                    "✅داری میترکونی👌🏻✅",
                    "✅حیرت آوره🤩✅",
                    "🎉",
                    "🥳",
                    "👏",
                ]
                # create a random message
                while True:
                    right_message = random.choice(right_messages)
                    if right_message in self.last_msg_right:
                        continue
                    else:
                        self.last_msg_right = right_message
                        update.message.reply_text(right_message)
                        data.level_up(update, context, condition=True) # level up, score up
                        button.main_btn(update, context)
                        data.score_up(update, context)
                        break


            # user send a wrong answer
            if update.message.text in data.wrong_answers(update, context):
                wrong_messages = [
                    "❌حواست کجاست؟❌",
                    "❌اشتباه بود❌",
                    "❌حواست رو جمع کن❌",
                    "❌اشتباه جواب دادی❌",
                    "❌حواست رو جمع کن خوشگله❌",
                    "❌حواست کجاست خوشگله؟❌",
                    "❌بیشتر دقت کن🙃❌",
                    "❌اشتباه بود🤷🏻‍♂️❌",
                    "❌از تو انتظار بیشتری دارما😇❌",
                    "❌اشتباه جواب دادی که، بیا واسه بعدی🙃❌"
                ]
                # create a random message
                while True:
                    wrong_message = random.choice(wrong_messages)
                    if wrong_message in self.last_msg_wrong:
                        continue
                    else:
                        self.last_msg_wrong = wrong_message
                        wrong_message = random.choice(wrong_messages)
                        update.message.reply_text(wrong_message)
                        data.level_up(update, context, condition=False) # level up, no change on score
                        data.lessons(update, context)
                        button.main_btn(update, context)
                        break
        
#        if update.message.reply_text in "result":
#            print("result")