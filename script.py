import telebot
import time

from telebot import types

from random import randint, choice
import text, buttons, functions
import main_menu, faq, teacher_account, student_account, dialog, verification, moodle, token

from multiprocessing import Process
import moodle


TOKEN = token.token
bot = telebot.TeleBot(TOKEN)

rootChat=token.rootChat
userrole = [0] #0 - guest, 1 - student, 2 - teacher

#moodle.get_course_info()
#moodle.verification_to_moodle("", [0])
#moodle.get_grades(4)
#moodle.verification_to_moodle("", 0)
main_menu.main(bot, userrole)
faq.main(bot)
teacher_account.main(bot)
dialog.main(bot)

@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, message.photo[0].file_id)

@bot.message_handler(content_types=['sticker'])
def photo(message):
    bot.send_message(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.chat.id)
    #bot.send_sticker(message.chat.id, "Не засмучуй свою маму, здавай лабораторні вчасно 😋")
    #bot.send_sticker(message.chat.id, "CAADAgADBwAD3k2QFhAuoyLqvM6KFgQ")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    print(message)



def reminder():
    while True:
        #bot.send_message(rootChat, "Не засмучуй свою маму, здавай лабораторні вчасно 😋")
        #bot.send_sticker(rootChat, "CAADAgADBwAD3k2QFhAuoyLqvM6KFgQ")
        bot.send_message(rootChat, "Викладач теж хоче на море 🏄, дотримуйся дедлайнів 🙃")
        bot.send_sticker(rootChat, "CAADAgADCAAD3k2QFnKGntVpmgoSFgQ")
        time.sleep(120)

if __name__ == '__main__':
    #p1 = Process(target=reminder, args=())
    #p1.start()
    #bot.set_update_listener(listener)  # register listener
    bot.polling()