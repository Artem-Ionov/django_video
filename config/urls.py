from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("videos/", include("videos.urls")),    # Вложенные url-сопоставления для приложения
    path("accounts/", include("django.contrib.auth.urls")),  # и для аутентификации
    # После выхода перенаправляем на страницу входа и не создаём шаблон для выхода
    path("logout/", LogoutView.as_view(next_page='login'), name='logout') 
]

# Раздача медиафайлов (только для разработки - в проде занимается сервер)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)