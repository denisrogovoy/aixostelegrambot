from telebot import types
import text, buttons, verification

def main(bot, userrole):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, text.bot_welcome, reply_markup=buttons.menu_main())
        bot.send_message(message.chat.id, '`Будь-ласка опиши свою проблему нижче, або скористайся меню.`', parse_mode="Markdown")
        bot.send_sticker(message.chat.id, "CAADAgADBQAD3k2QFob9Al_VZGbWFgQ")

    # ---------- MAIN MENU section ------------------------------
    @bot.message_handler(commands=['faq'])
    @bot.message_handler(regexp="(?i)(.*(FAQ).*)|(^⬅ Назад$)")
    def choose_question(message):
        bot.send_message(message.chat.id, 'Обери питання, яке тебе цікавить 👇: ', reply_markup=buttons.menu_faq())

    @bot.message_handler(commands=['sign_in'])
    @bot.message_handler(regexp="(?i).*(увійти)|(особистий).*кабінет.*")
    def send_sign_in(message):
        #global userrole

        if userrole[0]==0:
            bot.send_message(message.chat.id, text.authentication, reply_markup=buttons.verification())
            verification.main(bot, userrole)
        elif userrole[0]==1:
            bot.send_message(message.chat.id, "Ви увійшли до особистого кабінету студента 🤓", reply_markup=buttons.menu_student_account())
        elif userrole[0]==2:
            bot.send_message(message.chat.id, "Ви увійшли до особистого кабінету викладача 👨‍🏫", reply_markup=buttons.menu_teacher_account())

    @bot.message_handler(commands=['help'])
    @bot.message_handler(regexp="(?i).*((допомога)|(хелп)|(help)|(довідка)).*")
    def send_help(message):
        bot.send_message(message.chat.id, text.bot_help, reply_markup=buttons.menu_main())