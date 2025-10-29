from django.db import models

# Импортируем стандартную модель пользователя
from django.contrib.auth import get_user_model

# автоматически создаём класс пользователя
Юзер = get_user_model()
# Потом этого юзера будем привязывать в качестве свойства для других моделей

# Каждая модель (каждый класс) наследуются от стандартного класса джанго (принимает его стандартные свойства).
class Отзыв(models.Model):
    автор = models.ForeignKey(Юзер, on_delete=models.CASCADE)
    # Каждая переменная класса - это название поля (колонки таблицы)
    дата_поста = models.DateTimeField(
        # Это полеавтоматически считывает время компьютера и присваивает его в качестве значения в момент создания записи в базе данных (БД)
        auto_now=True
    )

    картинка = models.ImageField(
        # В скобках указываем, в какую папку загружать новые  картинки
        upload_to="медиа"
    )

    текст = models.TextField()

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        if len(self.текст) > 50:
            return self.текст[:50] + "..."
        return self.текст