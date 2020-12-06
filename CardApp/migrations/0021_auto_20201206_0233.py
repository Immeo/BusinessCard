# Generated by Django 3.1.3 on 2020-12-05 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardApp', '0020_auto_20201205_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='PricingCurrencyColumn1',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('RUB', 'RUB')], max_length=150, null=True, verbose_name='Изменить валюту первой колонки'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='PricingCurrencyColumn2',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('RUB', 'RUB')], max_length=150, null=True, verbose_name='Изменить валюту второй колонки'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='PricingCurrencyColumn3',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('RUB', 'RUB')], max_length=150, null=True, verbose_name='Изменить валюту третий колонки'),
        ),
    ]
