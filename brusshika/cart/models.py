from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=150, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                     verbose_name='Выберите категорию')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наменование')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    available = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        #index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

from django.db import models
from django.contrib.auth.models import User


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

"""
category - является экземпляром ForeignKey, содержит ключ на другую запись в базе данных, в нашем случае на Category. Все создаваемые продукты будут относится к какой-нибудь категории. on_delete=models.CASCADE - сообщает Django, что при удалении категории, будут удаляться все продукты, относящиеся к данной категории. related_name='products' - указывает имя обратной связи, так мы легко получим доступ ко всем продуктам категории.    
name - название продукта. Содержит данные CharField - строковое поле ограниченной длины, в нашем случае максимум 200 символов.   
slug - служит для построения удобочитаемых URLов.
image - фотография товара. Так как в параметрах стоит blank=True, значит поле не обязательно к заполнению. 
description - описание вашего продукта
price - цена товара. Тип поля DecimalField, которое хранит значение с фиксированной точностью. Парамаетр max_digits задает общее количество цифр, включая десятичные, decimal_places - количество цифр после запятой. 
available - наличие товара на складе. Тип BooleanField, так как есть два варианта True - в наличие, False - отсутствует на складе.
created - дата и время создания товара
updated - дата и время последнего изменения             
Класс Meta, метод __str__ и get_absolute_url несут такой же функционал, как и в модели Category.  
"""
