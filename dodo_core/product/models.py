from django.db import models


class Pizza(models.Model):
    """Моделька для Пицц"""

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveSmallIntegerField(verbose_name='цена')
    consist = models.TextField(verbose_name='состав')
    is_new = models.BooleanField()
    image = models.ImageField(upload_to='products', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'


"""

"""