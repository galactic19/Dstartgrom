from csv import list_dialects
from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']
    list_filter = ['author', 'created', 'updated']
    search_fields = ['text', 'created', 'updated']
    ordering = ['-created', '-updated']

admin.site.register(Photo, PhotoAdmin)

