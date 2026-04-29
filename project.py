import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
name = "семен"
promo = "pro20"
active = "1 год"
name_team = "greenkraft"
sender_mail = "ssemenyaev@yandex.ru"
recipient_mail = "ssemenyaev@yandex.ru"
LOGIN = os.getenv("YM_LOGIN")
PASSWORD = os.getenv("YM_PASSWORD")
subject = "акции от greenkraft"
letter = """
Здравствуйте, #user_name#!
Мы рады предложить вам специальное предложение на нашу продукцию! Мы дарим вам уникальный промокод, который дает скидку 20% на все наши товары.

Промокод: #promo#

Просто введите этот код при оформлении заказа на нашем сайте и получите скидку на любой товар в нашем ассортименте. Но не забудьте, что этот промокод действителен только до #data#.

Не упустите шанс сэкономить на покупке наших товаров! Мы надеемся, что вы найдете что-то, что подойдет именно вам.

С уважением,
Команда #name_team#!""".replace("#user_name#", name).replace("#promo#", promo).replace("#data#", active).replace("#name_team#", name_team)
head = f"""From: {sender_mail}
To: {recipient_mail}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";
"""
result = head + letter
result1 = result.encode("UTF-8")
server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
server.login(LOGIN, PASSWORD)
server.sendmail(sender_mail, recipient_mail, result1)
server.quit()