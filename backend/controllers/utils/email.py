from smtplib import SMTP
from email.message import EmailMessage
import requests
from os import path

from config import Config, BASE_DIR
from . import APIError

def get_bootstrap_css() -> str:
  try:
    return requests.get('https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css').text
  except:
    return ''

def send_email(subject: str, body: str, address: str, html: bool = False) -> bool:
  msg = EmailMessage()

  subject = 'En10da: ' + subject

  msg['Subject'] = subject
  msg['From'] = Config.SMTP_SENDER
  msg['To'] = address

  if html:
    body = open(path.join(BASE_DIR, 'emails/base.html'), 'r').read().replace('{body}', body).replace('{bootstrap_css}', get_bootstrap_css())
    msg.set_content("This email is written in HTML. It is recommended to use an HTML-compatible email client.\n\n" + body)
    msg.add_alternative(body, subtype="html")
  else:
    msg.set_content(body)

  try:
    with SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
      server.starttls()
      server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
      server.send_message(msg)
    return True
  except:
    raise APIError('Failed to send email', 500)
    return False
