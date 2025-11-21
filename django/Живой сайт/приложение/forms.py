# Стандартный импорт
from django.forms import ModelForm, CheckboxSelectMultiple

from .models import *

class ФормаОтзыва(ModelForm):
    class Meta:
        # ПРивязываем модель
        model = Отзыв

        # указываем поля, которые должен заполнять юзер
        fields = ["текст","картинка","тег"]

        # Если надо привязать значения Многие-ко-многим, то используем виджет
        widgets = {"тег": CheckboxSelectMultiple()}