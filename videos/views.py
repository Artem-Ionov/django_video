from django.shortcuts import render, redirect
from django.db.models import Q, F, Count
from django.contrib.auth.models import User
from .models import Video, Like

def display_list(request):
    """Получение всех видео, доступных данному пользователю"""

    if request.user.is_staff:
        videos = Video.objects.all().only("name")
    elif request.user.is_authenticated:
        # Для сложных условий используем Q-выражения
        videos = Video.objects.filter(Q(is_published=True)|Q(owner=request.user)).only("name")
    else:
        videos = Video.objects.filter(is_published=True).only("name")
    return render(request, "display_list.html", {"videos": videos})


def display_detail(request, pk):
    """Получение информации о конкретном видео"""
    video = Video.objects.get(pk=pk)
    return render(request, "display_detail.html", {"video": video})


def like_video(request, pk):
    video = Video.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(video=video, user=request.user)
    if created: # Пользователь может лайкнуть видео только 1 раз (+ constraint в БД)
        # F-выражения делают операцию атомарной и переносят её на уровень БД
        Video.objects.filter(pk=pk).update(total_likes=F("total_likes")+1)
    return redirect("display_detail", pk=pk)


def get_id(request):
    """Ссылка в шаблоне для данной функции появляется только для служебных пользователей"""
    videos = Video.objects.filter(is_published=True).only("name")
    return render(request, "get_id.html", {"videos": videos})


def get_statistics_groupby(request):
    """Получение списка пользователей с количеством их лайков с помощью groub_by"""
    users = User.objects.annotate(likes_count=Count("like"))
    return render(request, "get_statistics.html", {"users": users})


def get_statistics_subquery(request):
    """Получение списка пользователей с количеством их лайков с помощью subquery"""
    pass
