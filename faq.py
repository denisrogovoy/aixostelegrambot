from telebot import types
import text, buttons, functions, dialog
from random import randint, choice

def main(bot):
    dialog.main(bot)
    @bot.message_handler(commands=['tasks'])
    @bot.message_handler(regexp="(?i)^завдання.*")
    def tasks(message):
        bot.send_message(message.chat.id, 'Обери лабораторну роботу нижче 👇: ', reply_markup=buttons.menu_labs())

    @bot.message_handler(commands=['schedule'])
    @bot.message_handler(regexp="(?i).*(розклад).*")
    def labs_schedule(message):
        bot.send_message(message.chat.id, text.schedule, parse_mode="Markdown")

    @bot.message_handler(regexp="(?i).*((вимоги)|(звіт)).*")
    def requirements(message):
        bot.send_message(message.chat.id, text.requirements, parse_mode="Markdown")

    @bot.message_handler(regexp="(?i).*((робот.*)|(ssh.*)|(з wpar)).*")
    def help_ssh(message):
        bot.send_message(message.chat.id, text.connect_ssh, parse_mode="Markdown", disable_web_page_preview=False)
        bot.send_photo(message.chat.id, "AgACAgIAAxkBAAICs17X9Xx29jCEWyWdeeInpjs_PsC1AAJkrzEbEf3ASmESHIvivdvd4TF6kS4AAwEAAwIAA20AAwkaBAABGgQ")
        #[inline URL](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

    @bot.message_handler(regexp="(?i).*цікаві факти.*AIX.*")
    def facts_aix(message):
        bot.send_message(message.chat.id, choice(text.interesting_facts), parse_mode="Markdown")

    @bot.message_handler(regexp=".*До головного меню")
    def back_to_main_menu(message):
        bot.send_message(message.chat.id, 'Чим я можу тобі допомогти? 😋', reply_markup=buttons.menu_main())