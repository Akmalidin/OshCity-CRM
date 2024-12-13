from django.db import models
from decimal import Decimal



class OrderHistory(models.Model):
    shop = models.ForeignKey('product.Shop', on_delete=models.CASCADE, null=True)
    amount = models.FloatField()
    change = models.FloatField()
    discount = models.FloatField(null=True)
    profit = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'История заказа'
        verbose_name_plural = 'История заказа'

    def total_sum(self):
        total = sum((i.quantity * i.price_at_sale) for i in self.soldhistory_set.all())
        if self.discount:  # Если скидка есть, применяем её
            total -= Decimal(self.discount)  # Преобразуем скидку в Decimal
        return total
    
    def total_sum_without_discount(self):
        total = sum((i.quantity * i.price_at_sale) for i in self.soldhistory_set.all())
        return total


class SoldHistory(models.Model):
    order = models.ForeignKey(OrderHistory, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True) 
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Добавляем скидку
    change = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Например
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'История продаж'
        verbose_name_plural = 'История продаж'

    def total_sum(self):
        return self.quantity * self.product.sale_price

class Income(models.Model):
    shop = models.ForeignKey('product.Shop', on_delete=models.CASCADE, null=True)
    amount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'История поставок'
        verbose_name_plural = 'История поставок'

    def total_sum(self):
        total = sum((i.quantity * i.price_at_income) for i in self.incomehistory_set.all())
        return total

class IncomeHistory(models.Model):
    income = models.ForeignKey(Income, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Это поле должно существовать
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    change = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'История поставки'
        verbose_name_plural = 'История поставки'
    def __str__(self):
        return f"IncomeHistory {self.id}"
    def total_sum(self):
        return self.quantity * self.price_at_income
