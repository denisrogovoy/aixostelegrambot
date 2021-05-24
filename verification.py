import moodle, buttons, text, student_account, teacher_account

def main(bot, userrole):
    @bot.message_handler(content_types=['passport_data'])
    def listener(message):
        phone_number=message.passport_data["data"][0]["phone_number"]
        email=message.passport_data["data"][1]["email"]
        moodle.verification_to_moodle(email, userrole)
        #bot.send_message(message.chat.id, userrole[0])
        if userrole[0] == 0:
            bot.send_message(message.chat.id, text.error_registration, reply_markup=buttons.registration())
        elif userrole[0]==1:
            bot.send_message(message.chat.id, "Вітаємо, ви увійшли до особистого кабінету студента 🤓", reply_markup=buttons.menu_student_account())
            student_account.main(bot)

        elif userrole[0] == 2:
            bot.send_message(message.chat.id, "Вітаємо, ви увійшли до особистого кабінету викладача 👨‍🏫", reply_markup=buttons.menu_teacher_account())
            teacher_account.main(bot)
