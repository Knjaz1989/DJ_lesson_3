from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField('Имя', max_length=50)
    slug = models.SlugField('URL', unique=True)
    price = models.IntegerField('Цена')
    image = models.CharField('Ссылка на изображение', max_length=1000)
    release_date = models.CharField('Дата релиза', max_length=30)
    lte_exists = models.BooleanField('Наличие LTE')
