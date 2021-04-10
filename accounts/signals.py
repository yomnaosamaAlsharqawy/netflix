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
            'nfsysplus@gmail.com',
            [
                instance.username,
                # 'kareemahmed4996@gmail.com',
                'yomnaosama80@gmail.com',
                # 'mushihata@gmail.com',
            ],
            fail_silently=False,
        )


plans = [
    (1, 'Basic Plan', 120, 'Good', '1', 'PC', False, True),
    (2, 'Standard Plan', 165, 'Better', '2', 'PC', False, True),
    (3, 'Premium Plan', 200, 'Best', '3', 'PC', True, True),
]


def init_plans(sender, *args, **kwargs):
    for plan in plans:
        Plan(id=plan[0], title=plan[1], price=plan[2], video_quality=plan[3], screen_count=plan[4],
             supported_device=plan[5], unlimited_content=plan[6], cancel_anytime=plan[7]).save()


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
