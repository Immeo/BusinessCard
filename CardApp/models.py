from django.db import models
# Create your models here.

class edit_text(models.Model):
    TopFirstH1 = models.CharField(
        verbose_name='Изменить текст первого H1',
        max_length=150,
        blank=True,
        null=True,
    )
    TopFirstH2 = models.CharField(
        verbose_name='Изменить текст первого H2',
        default='Ваш текст',
        max_length=150,
        blank=True,
        null=True,
    )
    GetStartedBtn = models.CharField(
        verbose_name='Изменить текст первой кнопки',
        max_length=150,
        blank=True,
        null=True,
    )
    TopCardBlockTitle1 = models.CharField(
        verbose_name='Изменить название первого карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    TopCardBlockText1 = models.TextField(
        verbose_name='Изменить текст первого карт блока',
        blank=True,
        null=True,
    )
    TopCardBlockTitle2 = models.CharField(
        verbose_name='Изменить название второго карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    TopCardBlockText2 = models.TextField(
        verbose_name='Изменить текст второго карт блока',
        blank=True,
        null=True,
    )
    TopCardBlockTitle3 = models.CharField(
        verbose_name='Изменить название третьего карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    TopCardBlockText3 = models.TextField(
        verbose_name='Изменить текст третьего карт блока',
        blank=True,
        null=True,
    )
    TopCardBlockTitle4 = models.CharField(
        verbose_name='Изменить название четвертого карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    TopCardBlockText4 = models.TextField(
        verbose_name='Изменить текст четвертого карт блока',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.TopFirstH1
