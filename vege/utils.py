from django.utils.text import slugify
import uuid
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


#Generating slug for update_recipe url
def generate_slug(title:str)->str:
    from .models import Recipe
    title = slugify(title)

    while Recipe.objects.filter(slug = title).exists():
        title = f'{slugify(title)}-{str(uuid.uuid4())[:4]}'  #without str it throws error-TypeError: 'UUID' object is not subscriptable

    return title

#Sending email to the client
def send_email_to_client():
    subject = "Sending mail from Django server"
    message = "This mail is for testing purpose only from Django server mail"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['sukshamarya00007@gmail.com']
    send_mail(subject, message, from_email, recipient_list)


def send_email_with_attachment(subject, message, recipient_list, file_path):
    mail = EmailMessage(subject = subject, body = message, from_email = settings.EMAIL_HOST_USER, to = recipient_list)
    mail.attach_file(file_path)
    mail.send()
