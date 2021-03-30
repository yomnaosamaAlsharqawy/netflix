from django.contrib import admin
from .models import *


# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ("name",)
    # list_filter = ("year",)


admin.site.register(Movies, MovieAdmin)
admin.site.register(Casts)
admin.site.register(Tvshows)
admin.site.register(Genres)
admin.site.register(Moods)
admin.site.register(Seasons)
admin.site.register(Episodes)
