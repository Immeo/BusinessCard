from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.datetime_safe import date
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class bloc1(models.Model):
    title_text = models.CharField(
        verbose_name='Название',
        max_length=150,
        blank=True,
        null=True,
    )
    text_block = models.TextField(
        verbose_name='Название',
        blank=True,
        null=True,
    )

    def __str__(self):
        return
