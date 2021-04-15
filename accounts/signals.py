from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account, Plan, ProfileImage
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
            'nfmailsystem@gmail.com',
            [
                instance.username,
                # 'kareemahmed4996@gmail.com',
                'yomnaosama80@gmail.com',
                'mushihata@gmail.com',
            ],
            fail_silently=True,
        )


plans = [
    (1, 'Basic', 120, 'Good', '480px', '1', 'all'),
    (2, 'Standard', 165, 'Better', '1080px', '2', 'all'),
    (3, 'Premium', 200, 'Best', '4k+HDR', '3', 'all'),
]


def init_plans(sender, *args, **kwargs):
    for plan in plans:
        Plan(id=plan[0], title=plan[1], price=plan[2],video_quality=plan[3], resolution=plan[4], screen_count=plan[5],
             supported_device=plan[6]).save()


images = [
    (1, 'default', 'https://ia801509.us.archive.org/20/items/profiles_202104/default.png'),
    (2, 'chicken', 'https://ia801509.us.archive.org/20/items/profiles_202104/chicken.png'),
    (3, 'dog', 'https://ia801509.us.archive.org/20/items/profiles_202104/dog.png'),
    (4, 'hero', 'https://ia601509.us.archive.org/20/items/profiles_202104/hero.png'),
    (5, 'monster', 'https://ia601509.us.archive.org/20/items/profiles_202104/monster.png'),
    (6, 'penguin', 'https://ia801509.us.archive.org/20/items/profiles_202104/penguin.png'),
    (7, 'robot', 'https://ia601509.us.archive.org/20/items/profiles_202104/robot.png'),
]


def init_profile_images(sender, *args, **kwargs):
    for image in images:
        ProfileImage(id=image[0], name=image[1], image_url=image[2]).save()
