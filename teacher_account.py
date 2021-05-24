import subprocess
import text

def main(bot):
    @bot.message_handler(regexp="Статус WPARs.*")
    def status_wpars(message):
        a=subprocess.check_output(["lswpar"])
        bot.send_message(message.chat.id, a)

    @bot.message_handler(regexp="Зупинити WPARs.*")
    def stop_wpars(message):
        bot.send_message(message.chat.id, text.stop_wpars, parse_mode="Markdown")

    @bot.message_handler(regexp="Запустити WPARs.*")
    def stop_wpars(message):
        bot.send_message(message.chat.id, text.start_wpars, parse_mode="Markdown")

    @bot.message_handler(regexp="startwpar .*")
    def command_stop_wpars(message):
        text=message.text[9:].replace(",", "").split()
        print(text)
        for wpar in text:
            a = subprocess.check_output(["startwpar", wpar])
            bot.send_message(message.chat.id, a)
            bot.send_message(message.chat.id, "Wpar "+ wpar + " було запущено успішно 🚀")
        bot.send_message(message.chat.id, "Сommand completed successfully 💯")

    @bot.message_handler(regexp="stopwpar .*")
    def command_stop_wpars(message):
        text=message.text[9:].replace(",", "").split()
        print(text)
        for wpar in text:
            a = subprocess.check_output(["stopwpar", wpar])
            bot.send_message(message.chat.id, a)
        bot.send_message(message.chat.id, "Сommand was successful")