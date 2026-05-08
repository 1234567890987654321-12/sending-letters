import smtplib

name = input("Введите имя клиента: ")
promo = input("Введите промокод: ")
active = input("Срок действия (например, 1 год): ")
name_team = input("Название вашей команды: ")

sender_mail = input"Введите свою почту"
recipient_mail = input("Введите почту получателя: ")

LOGIN = input"Введите логин от почты" 
PASSWORD = input("Введите ваш пароль приложения Яндекс: ")

subject = input"Введите заголовок"

letter = f"""
Здравствуйте, {name}!
Мы рады предложить вам специальное предложение на нашу продукцию! Мы дарим вам уникальный промокод, который дает скидку 20% на все наши товары.

Промокод: {promo}

Просто введите этот код при оформлении заказа на нашем сайте и получите скидку на любой товар в нашем ассортименте. Но не забудьте, что этот промокод действителен только до {active}.

Не упустите шанс сэкономить на покупке наших товаров! Мы надеемся, что вы найдете что-то, что подойдет именно вам.

С уважением,
Команда {name_team}!"""

head = f"""From: {sender_mail}
To: {recipient_mail}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";
"""

result = (head + letter).encode("UTF-8")

try:
    print("Успешная отправка письма")
    server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    server.login(LOGIN, PASSWORD)
    server.sendmail(sender_mail, recipient_mail, result)
    server.quit()
    print("✅ Письмо успешно отправлено!")
except Exception as e:
    print(f"Ошибка: {e}")
