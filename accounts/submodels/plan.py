from django.db import models


VIDEO_QUALITY_CHOICES = [
    ('Good', 'Good'),
    ('Better', 'Better'),
    ('Best', 'Best'),
]

RES_CHOICES = [
    ("480px", "480px"),
    ("1080px", "1080px"),
    ("4k+HDR", "4k+HDR")
]

SCREEN_COUNT = [
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three')
]


class Plan(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    video_quality = models.CharField(choices=VIDEO_QUALITY_CHOICES, default=VIDEO_QUALITY_CHOICES[0][0], max_length=10,
                                     null=False)
    resolution = models.CharField(max_length=50, choices=RES_CHOICES, default=RES_CHOICES[0][0], null=False)
    screen_count = models.CharField(max_length=1, choices=SCREEN_COUNT, default=SCREEN_COUNT[0][0], null=False)
    supported_device = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# VideoQuality Model in the Database
# | id | type     | quality |
# | 1  | basic    |  480    |
# | 2  | standard |  720    |
# | 3  | premium  |  1080   |

# class VideoQuality(models.Model):
#     type = models.CharField(max_length=25)
#     quality = models.IntegerField()
