from django.db import models


class ItemModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    price = models.PositiveIntegerField(verbose_name='цена')

    def __str__(self):
        return f'({self.name}) ({self.price})'
