from telebot import types

def menu_main():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('FAQ ❓')
    itembtn2 = types.KeyboardButton('Особистий кабінет 🚪')
    itembtn3 = types.KeyboardButton('Довідка ⛑️')
    itembtn4 = types.KeyboardButton('Написати викладачу 📬')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    return markup

def menu_faq():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Завдання 📝')
    itembtn2 = types.KeyboardButton('Розклад лабораторних 🕑')
    itembtn3 = types.KeyboardButton('Вимоги до звіту ✔')
    itembtn4 = types.KeyboardButton('Робота з WPAR 🕹️')
    itembtn5 = types.KeyboardButton('⬅️До головного меню')
    itembtn6 = types.KeyboardButton('Цікаві факти про AIX 😲')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    return markup

def menu_teacher_account():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Запустити WPARs 🏃')
    itembtn2 = types.KeyboardButton('Зупинити WPARs ⛔')
    itembtn3 = types.KeyboardButton('⬅️До головного меню')
    itembtn4 = types.KeyboardButton('Статус WPARs ❓')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    return markup

def menu_student_account():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Запустити WPAR 🏃')
    itembtn2 = types.KeyboardButton('Зупинити WPAR ⛔')
    itembtn3 = types.KeyboardButton('Мої оцінки 💯')
    itembtn4 = types.KeyboardButton('Про курс ℹ️')
    itembtn5 = types.KeyboardButton('⬅️До головного меню')
    itembtn6 = types.KeyboardButton('Статус WPARs ❓')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    return markup

def menu_labs():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Лабораторна робота №1 🖥️')
    itembtn2 = types.KeyboardButton('Лабораторна робота №2 🧾')
    itembtn3 = types.KeyboardButton('Лабораторна робота №3 🔎')
    itembtn4 = types.KeyboardButton('Лабораторна робота №4 🖋️')
    itembtn5 = types.KeyboardButton('Лабораторна робота №5 🐚')
    itembtn6 = types.KeyboardButton('Лабораторна робота №6 🐍')
    itembtn7 = types.KeyboardButton('⬅ Назад')
    itembtn8 = types.KeyboardButton('Лабораторна робота №7 💻')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)
    return markup

def verification():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Пройти аутентифікацію", "http://54.237.179.112/verification/verification.html"))
    return markup

def registration():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Зареєструватися у Moodle", "http://54.237.179.112/moodle/login/index.php"))
    return markup