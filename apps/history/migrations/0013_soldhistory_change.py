# Generated by Django 5.1.2 on 2024-12-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0012_soldhistory_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldhistory',
            name='change',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
