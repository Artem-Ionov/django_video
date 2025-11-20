import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from videos.models import Video


class Command(BaseCommand):
    """Класс-команда для создания 100k видео и 10k пользователей"""

    def handle(self, *args, **options):
        users = []
        for i in range(10000):
            users.append(User(username=f"User {i}"))
        User.objects.bulk_create(users, batch_size=1000)
        self.stdout.write(f"Пользователи созданы")

        videos = []
        for i in range(100000):
            videos.append(Video(owner=random.choice(users), name=f"Видео {i}", is_published=True))
        Video.objects.bulk_create(videos, batch_size=1000)
        self.stdout.write("Видео для пользователей созданы")