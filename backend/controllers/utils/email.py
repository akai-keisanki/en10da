from smtplib import SMTP
from email.message import EmailMessage

from config import Config
from . import APIError

def send_email(subject: str, body: str, address: str) -> bool:
  msg = EmailMessage()
  msg['Subject'] = subject
  msg['From'] = Config.SMTP_USERNAME
  msg['To'] = address
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
