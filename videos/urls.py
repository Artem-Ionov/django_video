from django.urls import path
from .views import display_list, display_detail, like_video, get_id, get_statistics_groupby
from .views import get_statistics_subquery

urlpatterns = [
    path("", display_list, name="display_list"),
    path("videos/<int:pk>", display_detail, name="display_detail"),
    path("videos/<int:pk>/likes/", like_video, name="like_video"),
    path("videos/ids/", get_id, name="get_id"),
    path("videos/statistics-group-by/", get_statistics_groupby, name="get_statistics_groupby"),
    path("videos/statistics-subquery/", get_statistics_subquery, name="get_statistics_subquery"),
]