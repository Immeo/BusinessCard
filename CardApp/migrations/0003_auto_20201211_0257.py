# Generated by Django 3.1.3 on 2020-12-10 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardApp', '0002_auto_20201210_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myjob',
            name='slug',
            field=models.SlugField(default='TextTitle', help_text='Ссылка создается автоматически из заглавия продукта', max_length=200, unique=True, verbose_name='Ссылка на работу'),
        ),
    ]
