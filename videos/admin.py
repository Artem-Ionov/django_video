from django.contrib import admin
from .models import Video, VideoFile, Like

admin.site.register(VideoFile)
admin.site.register(Like)

@admin.register(Video)  # Регистрируем модель
class VideoAdmin(admin.ModelAdmin):
    """Класс для настройки отображения информации в админ-панели"""
    list_display = ["name", "owner", "created_at", "is_published", "total_likes"]

