# Стандартный образ python
FROM python:3.11

# Задание рабочей директории в контейнере (можно выбрать любое имя)
WORKDIR /django_video

# Копируем и устанавливаем зависимости (их вперёд для кэширования слоёв)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт (8000 - стандарт для Django, но можно любой свободный)
EXPOSE 8000

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

