from flask.ext.mail import Message
from app import mail
from flask import render_template
#from config import ADMINS
from threading import Thread
from app import app
from .decorators import async

def email_confirmation(mail_from):
    send_email("[microblog] your email was received!",
               app.config.ADMINS[0],
               [mail_from],
               render_template("email_confirmation.txt"),
               render_template("email_confirmation.html"))


def send_email_contact(sender, text_body):
    msg = Message('Email from blog', sender=sender, recipients=app.config.ADMINS[0])
    msg.body = text_body
    send_async_email(app, msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)


@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

