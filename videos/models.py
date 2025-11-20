from django.contrib.auth.models import User
from django.db import models


class Video(models.Model):

    name = models.CharField("Название", max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    is_published = models.BooleanField("Опубликовано", default=False)
    total_likes = models.IntegerField("Количество лайков", default=0)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self) -> str:
        return self.name


QUALITY = {"1": "HD", "2": "FHD", "3": "UHD"}


class VideoFile(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name="Видео")
    # Чтобы не заморачиваться с конкретными файлами при разработке, пока поставим blank
    file = models.FileField(
        "Файл", upload_to="videos", blank=True
    )  # Путь загрузки в MEDIA_ROOT
    quality = models.CharField(max_length=1, choices=QUALITY)

    class Meta:
        verbose_name = "Видеофайл"
        verbose_name_plural = "Видеофайлы"

    def __str__(self) -> str:
        return f"{self.video.name} ({self.get_quality_display()})"


class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name="Видео")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
        constraints = [
            models.UniqueConstraint(fields=["video", "user"], name="unique_like")
        ]

    def __str__(self) -> str:
        return f"Лайк {self.user.username} на {self.video.name}"
