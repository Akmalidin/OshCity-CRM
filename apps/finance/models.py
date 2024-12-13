from django.db import models
from django.utils import timezone

class Expend(models.Model):
    EXPEND_TYPE_CHOICES = [
        ('rent', 'Аренда'),
        ('utilities', 'Коммунальные услуги'),
        ('salaries', 'Зарплаты'),
        ('supplies', 'Поставки'),
        ('other', 'Другое')
    ]
    STATUS_CHOICES = [
        ('paid', 'Оплачен'),
        ('unpaid', 'Не оплачен'),
    ]
    shop = models.ForeignKey('product.Shop', on_delete=models.CASCADE, verbose_name="Магазин", null=True, blank=True)
    expend_type = models.CharField(max_length=50, choices=EXPEND_TYPE_CHOICES, verbose_name="Тип расхода")
    description = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(verbose_name="С даты")
    end_date = models.DateField(verbose_name="По дату")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid', verbose_name="Статус")
    is_salary_confirmed = models.BooleanField(default=False, verbose_name="Подтверждение зарплаты", null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="Пользователь", null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        start_date_formatted = self.start_date.strftime("%d.%m.%Y")
        end_date_formatted = self.end_date.strftime("%d.%m.%Y")
        return f"{self.get_expend_type_display()} {start_date_formatted} - {end_date_formatted}"