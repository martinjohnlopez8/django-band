from django.contrib import admin

from .models import Band, Album, Song, Member
# Register your models here.

admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Member)
