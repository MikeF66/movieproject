from django.db import models


class Film(models.Model):
    title = models.CharField('Название фильма', max_length=60)
    description = models.CharField('Описание фильма', max_length=240)
    content = models.TextField('Содержание фильма')
    review = models.CharField('Отзыв', max_length=240)
    date = models.DateField('Дата')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


