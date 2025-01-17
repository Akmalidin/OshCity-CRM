# Generated by Django 5.0.5 on 2024-11-05 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0005_orderhistory_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'История поставок',
                'verbose_name_plural': 'История поставок',
            },
        ),
        migrations.RemoveField(
            model_name='incomehistory',
            name='price',
        ),
        migrations.AddField(
            model_name='incomehistory',
            name='income',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='history.income'),
        ),
    ]
