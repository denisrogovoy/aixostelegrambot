import functions, buttons

def main(bot):
    @bot.message_handler(regexp="(?i).*(лабораторн).*\d.*")
    def send_labs(message):
        bot.send_message(message.chat.id, functions.send_task_for_lab(functions.parse_digits_from_text(message.text)), parse_mode="Markdown",
                         disable_web_page_preview=False, reply_markup=buttons.menu_labs())

    @bot.message_handler(regexp="(?i).*(дякую).*")
    def labs_schedule(message):
        bot.send_message(message.chat.id, "Нема за що, звертайся ще 😉.")

    @bot.message_handler(regexp="(?i).*не можу зробити лабораторну.*")
    def support(message):
        bot.send_message(message.chat.id, "У тебе все вийде 😉, я у тебе вірю 😘. Тримай шоколадку 🍫")