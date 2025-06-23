from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_welcome_email(email):
    logger.warning(f"[Celery Task] Email sending to: {email}")
    send_mail(
        subject="Welcome to our website",
        message="Thank you for registering with us",
        from_email=None,
        recipient_list=[email],
        fail_silently=False,
        
    )