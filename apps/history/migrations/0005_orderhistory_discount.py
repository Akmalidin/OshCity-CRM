# Generated by Django 5.0.5 on 2024-11-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_incomehistory_price_at_income_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='discount',
            field=models.FloatField(null=True),
        ),
    ]
