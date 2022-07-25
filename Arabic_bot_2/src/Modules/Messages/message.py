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
                                 text=f"{data.first_twiny_number(update, context)}. {update.effective_user.first_name} {update.effective_user.last_name}\nID: @{update.effective_user.username}")

        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

        sleep(1.5)

        update.message.reply_text(f"""سلام {update.effective_user.first_name} 🤗
چطوری؟ 😏
من رباتی هستم که کمکت می‌کنم عربی (لهجه لبنانی) خودت رو محک بزنی و ببینی سطح عربیت در چه حدی هست. 😲
حتی بهت میگم دقیقاً کجا ها ضعف داری و کمکت می‌کنم اون ضعف ها رو رو برطرف کنی.😦
بهت قول میدم اگه تا آخر با من همراه باشی عربیت کلی قوی تر میشه و عمرا تو صحبت کردن کم نمیاری.😉😎""")

        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

        sleep(8)

        update.message.reply_text("😉")

        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)


        sleep(3)

        update.message.reply_text("""
        حالا قراره چطوری این کار رو انجام بدیم؟؟🤓
خیلی ساده ...

من الان یه امتحان تستی ازت میگیرم که ۱۵ دقیقه هم وقتت رو نمیگیره، این امتحان شامل خیلی از مباحث مهم میشه که حتما باید بلد باشی. تنها کاری که باید انجام بدی اینه که دکمه شروع رو بزنی و امتحان رو شروع کنی.
خودم آخرش بهت نمره میدم و بهت میگم که اشکالاتت کجا بود و روی کدوم مباحث بیشتر باید کار کنی.😎💪🏻""")

        sleep(12)

        update.message.reply_text("""‼️حواست باشه فقط یه بار بیشتر نمیتونی امتحان بدی، پس سعی کن قششششنگ تمرکز کنی🤭""")

        sleep(1)

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

                sleep(2)

                if final == 100:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    sleep(10)
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
                    sleep(10)
                    update.message.reply_text("""بهت تبریک میگم🥳🥳
لهجه لبنانی ت تو سطح خوبی هست و مشخصه که روی خیلی از مباحث کار کردی و می‌دونی چی به چیه.😉
ولی خب باز هم ضعف هایی داشتی که من میتونم واست تقویتشون کمکت کنم😊
حواست باشه مهمترین قسمت امتحان دادن، پیدا کردن نقاط ضعفت و برطرف کردنشونه
که خیلی راحت با خوندن درسنامه ها ، میتونی لهجت رو تقویت کنی..
و همینکه مطالب بیشتری هست که میتونه تو رو به سطح بالاتری برسونه..""")

                if 70 > final > 40:
                    test = data.read_lessons(update, context)
                    test = test.split(", ")
                    testi = Counter(test)
                    s = "\n⚠️".join(testi.keys())
                    s = s.replace('None', '')
                    s = "🔰 این ها مواردی هست که تو درشون ضعف داری و باید بیشتر روی اون ها کار کنی:\n" + s 
                    update.message.reply_text(s)

                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    sleep(10)
                    update.message.reply_text("""✅✅✅✅✅
آفرین، خیلی امتحان خوبی دادی😁👌
نمره ت خوبه، این نشون میده خوب داری میری جلو و مباحث رو یاد می‌گیری، این امتحان از موضوعات مختلفی بود، ولی تو تونستی بیشترش رو درست جواب بدی. این عالیه🤗
ولی خودت بهتر می‌دونی که نیاز به کار کردن داری و باید بیشتر لهجه لبنانی رو تمرین کنی.
ولی خبر خوب اینحاست که نمیخواد جای دوری بری، من درسنامه های این سوالارو بهت یاد میدم، با کلی مطلب دیگه که تورو به سطح بالاتری میبره..""")


                if final < 40:
                    test = data.read_lessons(update, context)
                    test = test.split(", ")
                    testi = Counter(test)
                    s = "\n⚠️".join(testi.keys())
                    s = s.replace('None', '')
                    s = "🔰 این ها مواردی هست که تو درشون ضعف داری و باید بیشتر روی اون ها کار کنی:\n" + s 
                    update.message.reply_text(s)

                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    sleep(10)
                    update.message.reply_text("""✅✅✅✅✅
آفرین، امتحان خوبی دادی😃
از نمره ت مشخصه تازه لهجه لبنانی رو شروع کردی و اول مسیری. نمره ای که به دست آوردی نسبت به معلوماتت عالیه. و مطمئنم بیشتر بلدی ولی هنوز واست تثبیت نشدن..
و هنوزم خیلی چیز ای دیگه هست که باید یاد بگیری.😁👌
بیا دنبالم، درسنامه هارو بخون و اطلاعاتت رو تثبیت کن، واسه تقویت کردن لهجت فقط یه قدم دیگه بردار، من کمکت میکنم.😉""")


                context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                sleep(15)


                update.message.reply_text("""ولی قبلش یه خاطره برات تعریف کنم ...

چند وقت پیش یه کشور عربی بودم. به واسطه کاری که داشتم با خیلی ها باید صحبت می‌کردم و مترجمی هم نداشتم که کمکم کنه، پس مجبور بودم خودم گلیم خودم رو از آب بکشم بیرون و سعی کردم به این موقعیت به عنوان یه فرصت یادگیری نگاه کنم، کاری که انجام دادم این بود که هر چیزی رو که بلد نبودم و خیلی بهش نیاز داشتم رو یادداشت کنم. مثلا فهمیدم که من اصلااا اعداد رو بلد نیستم، پس یادداشت می‌کردم باید اعداد رو تمرین کنم. (بماند که همش نگران بودم نکنه وقتی بفهمن عرب نیستم و عربیم هم خیلی‌خوب نیست سرم کلاه بذارن😅😂)

وقتی میخواستم چیزی بخرم میپرسیدم قیمت چنده؟ مغازه دار یه چیزی میگفت و مهم الکی مگفتم اوکی و یه پول درشت بهش میدادم که نخوام پول رو خودم بشمارم و فقط بقیه پول رو میگرفتم😅😅""")

                sleep(17)
                context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_PHOTO)
                sleep(5)

                context.bot.send_photo(update.effective_chat.id,
                                        caption="این لباسی هست که اونجا میخواستم قیمت کنم و بخرم، ولی وقتی فروشنده قیمتش رو بهم گفت اصلا متوجه نشدم و هنوز هم نمیدونم قیمتش چند بود🥲😂",
                                        photo='https://github.com/Htyior/-Music_game-_BOT/raw/main/photo_2022-07-25_11-06-39.jpg'
                                    )

                context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                sleep(8)


                update.message.reply_text("""وقتی برگشتم ایران فقط یک ساعت وقت گذاشتم و اعداد عربی رو یادگرفتم، و سعی کردم تا می‌تونم اعداد رو با خودم تکرار کنم.🤓

نتیجه چی شد؟🤔

تو سفر بعدی انقدر اعداد برام راحت بود و عالی یادگرفته بودم که بقیه هم از من کمک میخواستن و حتی جمع و تفریق پول ها رو سریع تر از خود عرب ها انجام می‌دادم 😄✌🏻

من نقطه ضعفای خودمو دنبال کردم و به این مرحله رسیدم😎

اعداد فقط یک مثال بود که متوجه بشی چقدر مهمه که بتونی ضعف هایی که داری رو شناسایی کنی و اونا رو به نقاط قوتت تبدیل کنی.✌🏻""")


                context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                sleep(20)


                update.message.reply_text("""🔹من واست یه مرجع لبنانی ساختم، که مادام العمر دستته و راحت میتونی به هر درسنامه ای که میخوای دسترسی داشته باشی..✌️

🔹اطلاعاتی که خودم بلدم رو در اختیارت میذارم که تو هم راحت بتونی خودت رو به سطحای بالاتر برسونی..😉

🔹واست کنارش اصطلاحات و کلی کلمه گذاشتم که دایره لغاتت هم بره بالا..🤯

🔹فکرشو بکن چقد میتونی سریعتر ضعفای لهجت رو تقویت کنی و تازه کنارش کلی مطلب دیگه هم یاد بگیری..😍

🔷اینا بخشی از خدمات من هست:
✅ کلمات(بر محوریت مکان و موضوع)
✅ قواعد
✅ کلیپ های کوتاه عربی همراه با متن عربی و فارسی
✅ آهنگ های لبنانی
✅ پادکست های لبنانی

💯مهم تر از همه ...
✅ خودم کنارت هستم و تجربه های خیلی مفید خودم و بقیه کسایی که مسیر تورو خیلی وقت پیش رفتند رو در اختیارت میذارم و کمکت میکنم بتونی زودتر رشد کنی.😎😊🤗


دیگه منتظر چی هستی؟!
زودتر از بقیه پیشرفت کن💪🏻، منم کنارتم..🥳""")


                context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                sleep(20)

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