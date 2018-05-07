from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# from full_web_app.settings import EMAIL_FROM

def random_str(randomlenght=8):
    str = ''
    chars = 'ABCDEFabcdef123456'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlenght):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(8)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "Online register"
        email_body = "This is register link: http://127.0.0.1:8000/active/{0}".format(code)
        # send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        email_send = EmailMessage(email_title,email_body,to=[email])
        email_send.send()
        # if send_status:
        #     pass
    elif send_type =="forget":
        email_title = "Reset password"
        email_body = "This is the link for getting password back: http://127.0.0.1:8000/reset/{0}".format(code)
        email_send = EmailMessage(email_title, email_body, to=[email])
        email_send.send()
        # send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # if send_status:
        #     pass
