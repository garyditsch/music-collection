from django.contrib import admin

# Register your models here.

from .models import Track, Genre, Album

admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Genre)
