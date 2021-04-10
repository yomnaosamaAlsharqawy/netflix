from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from django.core.mail import send_mail


@receiver(post_save, sender=Account)
def account_registration_handler(sender, instance, created, *args, **kwargs):
    email_message = f"Dear {instance.username.split('@')[0]},\n\n\n\
Welcome to Netflix Plus! Your account has been created successfully.\n\n\
You can now start watching your favorite Movies and TV Shows! \n\n\
This is an automated message, please do not reply. \n\n\n\
Kind Regards, \n\
ITI Netflix Plus Team"

    if created:
        send_mail(
            'ITI Netflix Plus Account',
            email_message,
            'nfsysplus@gmail.com',
            [
                instance.username,
                # 'kareemahmed4996@gmail.com',
                'yomnaosama80@gmail.com',
                # 'mushihata@gmail.com',
            ],
            fail_silently=False,
        )
