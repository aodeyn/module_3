def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" in recipient and "@" in sender:
        if ((sender.find('.com') > -1 or sender.find('.ru') > -1 or sender.find('.net') > - 1) and
                (recipient.find('.com') > -1 or recipient.find('.ru') > -1 or recipient.find('.net') > -1)):
            if sender == recipient:
                return print("Нельзя отправить письмо самому себе!")
            if sender != "university.help@gmail.com":
                return print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, " на адрес ",recipient)
            return print("Письмо успешно отправлено с адреса ", sender, " на адрес ", recipient)
        else:
            return print("Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com' )
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
