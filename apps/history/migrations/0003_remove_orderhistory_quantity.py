# Generated by Django 5.1.2 on 2024-10-28 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_orderhistory_soldhistory_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhistory',
            name='quantity',
        ),
    ]
