import text, moodle

def main(bot):
    @bot.message_handler(regexp=".*оцінки.*")
    def send_marks(message):
        grades=moodle.get_grades(8)
        bot.send_message(message.chat.id, grades, parse_mode="Markdown")

    @bot.message_handler(regexp="Про курс .*")
    def course_info(message):
        course_name, summary=moodle.get_course_info()
        #print(course_name)
        #print(summary)
        bot.send_message(message.chat.id, "*Назва курсу: {0}*\n\n_Про курс: _{1}".format(course_name, summary), parse_mode="Markdown")