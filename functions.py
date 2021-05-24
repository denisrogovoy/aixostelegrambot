import text

def parse_digits_from_text(text):
    digit = ""
    for i in text:
        if i.isdigit():
            digit += i
    return int(digit)

def send_task_for_lab(number):
    if (0 < number < 8):
        return text.labs_and_links[number]
    else:
        return "Оберіть потрібну лабораторну роботу нижче: "