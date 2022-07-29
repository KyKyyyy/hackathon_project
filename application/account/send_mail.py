from django.core.mail import send_mail


def send_confirmation_email(code, email):
    full_link = f'Вас приветствует магазин мебели прошу вас подтвердить свою регистрацию по этой сыллке ' \
                f' http://localhost:8000/api/v1/account/activate/{code}'

    send_mail(
        'Furniture shop ',
        full_link,
        'damirbekovemir@gmail.com',
        [email]
    )