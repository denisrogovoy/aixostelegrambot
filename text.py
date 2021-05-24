schedule = "*Лабораторна група 1*: \n"\
                "\t\tпонеділок, середа: 14:05-16:40\n"\
                "*Лабораторна група 2*\n"\
                "\t\tвівторок, п'ятниця: 12:20-13:55\n"\
                "_Графік складання лабораторних робіт:_\n"\
                "*Лабораторна робота №1* - 3 лютого - 14 лютого\n"\
                "*Лабораторна робота №2* - 17 лютого - 28 лютого\n"\
                "*Лабораторна робота №3* - 2 березня - 13 березня\n"\
                "*Лабораторна робота №4* - 16 березня - 27 березня\n"\
                "*Лабораторна робота №5* - 30 березня - 10 квітня\n"\
                "*Лабораторна робота №6* - 13 квітня - 24 квітня\n"\
                "*Лабораторна робота №7* - 27 квітня - 8 травня\n"\
                "_До складання боргів - 11 травня - 22 травня_\n\n"\
                "*Залік - 25 травня 2020*"

requirements = "*1) Звіт має бути обов'язково підписаний (містити прізвище та ім'я студента);*\n"\
                "*2) Шрифт:* Times New Roman, *розмір:* 14, *інтервал:* 1.5;\n"\
                "*3)* Звіт має бути збереженим у форматі *.pdf*, розмір має бути не більше 2МБ;\n"\
                "*4)* Звіт має бути обов'язково *завантаженим* у систему *Moodle Education*;\n"\
                "*5)* Звіт *має містити скріншоти* виконання лабораторної роботи, сценаріїв та команд;\n"\
                "*6) За сдачу не свого звіту* за виконання лабораторної роботи ставиться *0 балів*;\n"\
                "*7) За не вчасну здачу* лабораторної роботи за кожну неділю *знімається 2 бали*."

connect_ssh = "*1)* Треба [завантажити PuTTY]() або будь-який інший ssh клієнт;\n"\
              "*2)* Треба у поле Host Name написати наступне _login@ipAddress_, де _login_ - ваш логін, а _ipAddress_ - ip адрес вашого WPAR (10.0.41.X);\n"\
              "*3)* Натиснути кнопку _Open_ (треба підключитися)."

interesting_facts = ["Перша версія ОС AIX (Advanced Interactive eXecutive англ. /ˌeɪaɪˈɛks/) вийшла у 1986 році 🕙 та мала назву AIX/RT 2. "\
                     "Вона була побудованана базі UNIX System V 🙇",

                     "У ОС AIX є помічник SMIT (System Management Interface Tool). З його допомогою можна не вводити довгі команди з великою кількістю "\
                     "аргументів 😉. Помічник SMIT представлений у графічному інтерфейсі, у Web-застосуванні та у командному рядку. Він значно полегшує "\
                     "роботу з ОС AIX та пришвидшує її адміністрування 😋. Без нього це б було робити набагато складніше 🥴. Для того, щоб запустити помічник "\
                     "SMIT у командному рядку треба виконати команду smitty або smit -c. 🏃",

                     "У ОС AIX є графічна оболонка, вона має назву CDE (Common Desktop Environment) 🌌. Тривалий час була вона була класичною графічною оболонкою"\
                     "для ОС Unix 🕓. Але з часом у більшості ОС Unix була замінена на графічні оболонки GNOME та KDE 🔄.",

                     "Згідно даних компанії [\"Enlyft\"](https://enlyft.com/tech/products/ibm-aix) 🌐 ОС AIX у світі використовує 9,321 компанія 🏢 (це скаладає "\
                     "0,47% від інших операційних систем 🌍).",

                     "У ОС AIX є своя технологія віртуалізації 🛠️, вона називається WPAR (Workload Partitions) 🌀. Вона підтримується у ОС AIX v.6.1 та вище 👾."]

labs_and_links = { 1:  "[Лабораторна робота №1](https://drive.google.com/file/d/1kRq5fmN-wINjBuxDN6hmm4EsQ3I_FLi8/view?usp=sharing)",
                   2: "[Лабораторна робота №2](https://drive.google.com/file/d/1hGwd5RDr4JoFCjK9e8r0AZrqNLXN7irE/view?usp=sharing)",
                   3: "[Лабораторна робота №3](https://drive.google.com/file/d/1QFDP9wbosKtVpohAzqeWz2kEDyJbIMKN/view?usp=sharing)",
                   4: "[Лабораторна робота №4](https://drive.google.com/file/d/1q-qu8N54GU_xlXGgTob64Y5pM26J4RNm/view?usp=sharing)",
                   5: "[Лабораторна робота №5](https://drive.google.com/file/d/1lmv07r3PLgtEHhoWQKFpadF5z0bS_X-C/view?usp=sharing)",
                   6: "[Лабораторна робота №6](https://drive.google.com/file/d/1JF61tUmlc4y397-4nAfYLaAmKfYs1cTE/view?usp=sharing)",
                   7: "[Лабораторна робота №7](https://drive.google.com/file/d/1ZjaHuOvCq4HJ04wQOGK09LeQukqhwSqF/view?usp=sharing)"}

authentication = "Для того, щоб увійти у свій особистий кабінет пройдіть аутентифікацію за допомогою навчальної платформи Moodle 🎓 та Telegram Passport 🛂."

error_registration = 'Ви не зареєстровані у курсі "Програмування для UNIX-систем" ⚠! Будь-ласка, зареєструйтеся у навчальній платформі Moodle 🎓 та зв\'яжіться з вашим'\
               ' викладачем, щоб він додав вас до курсу 👾.'

stop_wpars = "Для зупинки WPARs введіть команду *stopwpar* та відповідні номери WPARs, які ви хочете зупинити (Наприклад: `stopwpar stud1, stud10, stud15` "\
             "або `stopwpar ALL` для зупинки усіх WPARs"

start_wpars = "Для запуску WPARs введіть команду *startwpar* та відповідні номери WPARs, які ви хочете запустити (Наприклад: `startwpar stud1, stud10, stud15` або "\
              "`startwpar ALL` для запуску усіх WPARs"

bot_welcome = "Привіт! Мене звати Дейв 😊. Я віртуальний помічник викладача 👨‍💼 та адміністратор ОС AIX 🖥️. Чим я можу тобі допомогти?"

bot_help = "/start - Почати спілкування з ботом\n"\
           "/faq - Найчастіші питання\n"\
           "/sign_in - Увійти в особистий кабінет\n"\
            "/help - Довідка\n"\
            "/feedback - Зворотній зв'язок з викладачем\n"
