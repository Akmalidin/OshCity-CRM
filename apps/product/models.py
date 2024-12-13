from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

# comment
class Shop(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='shops', verbose_name='Изображение')
    name = models.CharField(max_length=100, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
class Product_brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название бренда')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)
    brand = models.ForeignKey(Product_brand, on_delete=models.CASCADE, verbose_name='Бренд', null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена покупки')
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)], null=True, blank=True,
        verbose_name='Продажная цена'
    )
    image = models.ImageField(null=True, blank=True, upload_to='products', verbose_name='Изображение', default='products/default_product.png')
    bar_code = models.CharField(max_length=100, null=True, verbose_name='Штрихкод', unique=True)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='Количество')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def in_stock(self):
        return self.quantity > 0

    def month_sales(self):
        return sum(i.quantity for i in self.soldhistory_set.filter(created__year=datetime.now().year, created__month=datetime.now().month))
