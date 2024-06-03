from django.contrib import admin
from .models import DownloadedImage
from django.utils import timezone


@admin.register(DownloadedImage)
class DownloadedImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'image_url', 'downloaded_at')
