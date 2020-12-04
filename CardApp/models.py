from django.db import models
# Create your models here.


class TopNavAndHero(models.Model):
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
        
    def __str__(self):
        return self.TopFirstH1


class AboutSection(models.Model):
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

    def __str__(self):
        return self.AboutSectionH2


class CountsSection(models.Model):
    CounterNumber1 = models.IntegerField(
        verbose_name='Изменить цифры счетчика второго сектора 1',
        blank=True,
        null=True,
    )
    CounterTitle1 = models.CharField(
        verbose_name='Изменить текст под счетчиком второго сектора 1',
        max_length=150,
        blank=True,
        null=True,
    )
    CounterNumber2 = models.IntegerField(
        verbose_name='Изменить цифры счетчика второго сектора 2',
        blank=True,
        null=True,
    )
    CounterTitle2 = models.CharField(
        verbose_name='Изменить текст под счетчиком второго сектора 2',
        max_length=150,
        blank=True,
        null=True,
    )
    CounterNumber3 = models.IntegerField(
        verbose_name='Изменить цифры счетчика второго сектора 3',
        blank=True,
        null=True,
    )
    CounterTitle3 = models.CharField(
        verbose_name='Изменить текст под счетчиком второго сектора 3',
        max_length=150,
        blank=True,
        null=True,
    )
    CounterNumber4 = models.IntegerField(
        verbose_name='Изменить цифры счетчика второго сектора 4',
        blank=True,
        null=True,
    )
    CounterTitle4 = models.CharField(
        verbose_name='Изменить текст под счетчиком второго сектора 4',
        max_length=150,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.CounterTitle1


class AboutVideoSection(models.Model):
    AboutVideoSectionPlug = models.ImageField(
        verbose_name='Картинка для заглушки видео',
        help_text='Рекомендованное разрешение для заглушки: 1024 х 760',
        upload_to='AboutVideoSection'
    )
    AboutVideoSectionUrl = models.CharField(
        verbose_name='Ссылка на видео',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutVideoSectionH3 = models.CharField(
        verbose_name='Изменить заговолок',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutVideoSectionP = models.TextField(
        verbose_name='Текст под заговолком',
        blank=True,
        null=True
    )
    AboutVideoSectionLi1 = models.CharField(
        verbose_name='Изменить текст пункта 1',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutVideoSectionLi2 = models.CharField(
        verbose_name='Изменить текст пункта 2',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutVideoSectionLi3 = models.CharField(
        verbose_name='Изменить текст пункта 3',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutVideoSectionLi4 = models.CharField(
        verbose_name='Изменить текст пункта 4',
        max_length=150,
        blank=True,
        null=True,
    )
    AboutVideoSectionEndP = models.TextField(
        verbose_name='Изменить текст в конце секции',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.AboutVideoSectionH3

class reviews(models.Model):
    TextReviews = models.TextField(
        verbose_name='Текст отзыва',
        blank=True,
        null=True,
    )
    PhotoReviews = models.ImageField(
        verbose_name='Фото клиента',
        help_text='Рекомендованное разрешение для фото: 400 х 400',
        upload_to='reviews'
    )
    FioReviews = models.CharField(
        verbose_name='Имя фамилия клиента',
        max_length=250,
        blank=True,
        null=True,
    )
    RoleReviews = models.CharField(
        verbose_name='роль клиента',
        max_length=250,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.FioReviews


class team(models.Model):
    PhotoTeam = models.ImageField(
        verbose_name='Фото сотрудника',
        help_text='Рекомендованное разрешение для фото: 400 х 400',
        upload_to='team'
    )
    FioTeam = models.CharField(
        verbose_name='Имя фамилия сотрудника',
        max_length=250,
        blank=True,
        null=True,
    )
    RoleTeam = models.CharField(
        verbose_name='роль сотрудника',
        max_length=250,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.FioTeam
