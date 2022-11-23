from django.db import models

class Item(models.Model):
    name = models.CharField(
        'Название',
        max_length=256,
        help_text='Введите название',
        db_index=True,
        unique=True
    )
    description = models.TextField(
        'Описание',
        help_text='Опишите товар',
        max_length=3000
    )
    price = models.PositiveIntegerField(
        'Стоимость'
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        return self.name
