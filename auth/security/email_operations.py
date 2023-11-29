import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(
    sender_email_param,
    sender_password_param,
    recipient_email_param,
    subject_param,
    body_param,
):
    message = MIMEMultipart()
    message["From"] = sender_email_param
    message["To"] = recipient_email_param
    message["Subject"] = subject_param

    message.attach(MIMEText(body_param, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()

        server.login(sender_email_param, sender_password_param)

        server.sendmail(sender_email_param, recipient_email_param, message.as_string())
