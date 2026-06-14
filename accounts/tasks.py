from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(
    bind=True,
    retry_backoff=5,
    name="accounts.email_notification"
)

def send_email_notification(self, recipient_email):
    send_mail(
        subject="Welcome",
        message="Thanks for signing up!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient_email],
        fail_silently=False
    )
