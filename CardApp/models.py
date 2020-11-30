from django.db import models
# Create your models here.

class edit_text(models.Model):
    TopLiNav1 = models.CharField(
        verbose_name='Изменить текст пункта меню 1',
        max_length=150,
        blank=True,
        null=True,
    )
    TopLiNav2 = models.CharField(
        verbose_name='Изменить текст пункта меню 2',
        max_length=150,
        blank=True,
        null=True,
    )
    TopLiNav3 = models.CharField(
        verbose_name='Изменить текст пункта меню 3',
        max_length=150,
        blank=True,
        null=True,
    )
    TopLiNav4 = models.CharField(
        verbose_name='Изменить текст пункта меню 4',
        max_length=150,
        blank=True,
        null=True,
    )
    TopLiNav5 = models.CharField(
        verbose_name='Изменить текст пункта меню 5',
        max_length=150,
        blank=True,
        null=True,
    )
    TopLiNav6 = models.CharField(
        verbose_name='Изменить текст пункта меню 6',
        max_length=150,
        blank=True,
        null=True,
    )
    TopLiNav7 = models.CharField(
        verbose_name='Изменить текст пункта меню 7',
        max_length=150,
        blank=True,
        null=True,
    )
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
    AboutSectionH2 = models.CharField(
        verbose_name='Изменить название тега h2 во второй секции',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutSectionP = models.TextField(
        verbose_name='Изменить текст под тегом h2 во второй секции',
        blank=True,
        null=True,
    )
    AboutSectionTextArea1 = models.TextField(
        verbose_name='Изменить текст первой колонки во второй секции',
        blank=True,
        null=True,
    )
    AboutSectionTextArea2 = models.TextField(
        verbose_name='Изменить текст второй колонки во второй секции',
        blank=True,
        null=True,
    )
    AboutLi1 = models.CharField(
        verbose_name='Изменить текст пункта второго сектора 1',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutLi2 = models.CharField(
        verbose_name='Изменить текст пункта второго сектора 2',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutLi3 = models.CharField(
        verbose_name='Изменить текст пункта второго сектора 3',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutButton = models.CharField(
        verbose_name='Изменить текст кнопки второго сектора',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutCounterNumber1 = models.IntegerField(
        verbose_name='Изменить цифры счетчика второго сектора 1',
        blank=True,
        null=True,
    )
    AboutCounterTitle1 = models.CharField(
        verbose_name='Изменить текст под счетчиком второго сектора 1',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutCounterNumber2 = models.IntegerField(
        verbose_name='Изменить цифры счетчика второго сектора 2',
        blank=True,
        null=True,
    )
    AboutCounterTitle2 = models.CharField(
        verbose_name='Изменить текст под счетчиком второго сектора 2',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutCounterNumber3 = models.IntegerField(
        verbose_name='Изменить цифры счетчика второго сектора 3',
        blank=True,
        null=True,
    )
    AboutCounterTitle3 = models.CharField(
        verbose_name='Изменить текст под счетчиком второго сектора 3',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutCounterNumber4 = models.IntegerField(
        verbose_name='Изменить цифры счетчика второго сектора 4',
        blank=True,
        null=True,
    )
    AboutCounterTitle4 = models.CharField(
        verbose_name='Изменить текст под счетчиком второго сектора 4',
        max_length=150,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.TopFirstH1
