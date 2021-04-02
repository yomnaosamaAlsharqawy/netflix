from django.db import models


class Plan(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2)
    video_quality = models.CharField(choices=('Good', 'Better', 'Best'), default='Good', null=False)
    resolution = models.IntegerField(choices=(480, 720, 1080), default=480, null=False)
    screen_count = models.IntegerField(choices=(1, 2, 4), default=1, null=False)
    supported_device = models.CharField(max_length=50)
    unlimited_content = models.BooleanField(default=False)
    cancel_anytime = models.BooleanField(default=False)


# VideoQuality Model in the Database
# | id | type     | quality |
# | 1  | basic    |  480    |
# | 2  | standard |  720    |
# | 3  | premium  |  1080   |

# class VideoQuality(models.Model):
#     type = models.CharField(max_length=25)
#     quality = models.IntegerField()
