from django.db import models


VIDEO_QUALITY_CHOICES = [
    ('Good', '480'),
    ('Better', '720'),
    ('Best', '1080'),
]

SCREEN_COUNT = [
    ('One', '1'),
    ('Two', '2'),
    ('Three', '3')
]


class Plan(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=3)
    video_quality = models.CharField(choices=VIDEO_QUALITY_CHOICES, default=VIDEO_QUALITY_CHOICES[0][0], max_length=10,
                                     null=False)
    # resolution = models.IntegerField(choices=(480, 720, 1080), default=480, null=False)
    screen_count = models.IntegerField(choices=SCREEN_COUNT, default=SCREEN_COUNT[0][0], null=False)
    supported_device = models.CharField(max_length=50)
    unlimited_content = models.BooleanField(default=False)
    cancel_anytime = models.BooleanField(default=False)

    def __str__(self):
        return str({self.title})


# VideoQuality Model in the Database
# | id | type     | quality |
# | 1  | basic    |  480    |
# | 2  | standard |  720    |
# | 3  | premium  |  1080   |

# class VideoQuality(models.Model):
#     type = models.CharField(max_length=25)
#     quality = models.IntegerField()
