from django.shortcuts import render
from .models import Video

def display_list(request):
    """Получение всех видео"""

    videos = Video.objects.all()
    return render(request, "display_list.html", {"videos": videos})
