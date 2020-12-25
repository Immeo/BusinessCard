from django.db import models
from pytils import translit
from django.utils.datetime_safe import date
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# from django.utils.translation import ugettext_lazy as _

# Create your models here.

class logo(models.Model):
    logotype = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return 'Ваше лого'

class nav(models.Model):
    nav = models.CharField(
        verbose_name='Изменить текст пункта меню 1',
        max_length=150,
        blank=True,
        null=True,
    )
    SlugNav = models.CharField(
        verbose_name='Ссылка или якорь пункта меню',
        max_length=400,
        unique=True,
    )

    def __str__(self):
        return self.nav


class hero(models.Model):
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
    # AboutSectionH2 = models.CharField(
    #     verbose_name='Изменить название тега h2 во второй секции',
    #     max_length=150,
    #     blank=True,
    #     null=True,
    # )
    AboutSectionP = models.TextField(
        verbose_name='Изменить текст под тегом h2 во второй секции',
        blank=True,
        null=True,
    )
    # AboutSectionTextArea1 = models.TextField(
    #     verbose_name='Изменить текст первой колонки во второй секции',
    #     blank=True,
    #     null=True,
    # )
    # AboutSectionTextArea2 = models.TextField(
    #     verbose_name='Изменить текст второй колонки во второй секции',
    #     blank=True,
    #     null=True,
    # )
    # AboutLi1 = models.CharField(
    #     verbose_name='Изменить текст пункта второго сектора 1',
    #     max_length=150,
    #     blank=True,
    #     null=True,
    # )
    # AboutLi2 = models.CharField(
    #     verbose_name='Изменить текст пункта второго сектора 2',
    #     max_length=150,
    #     blank=True,
    #     null=True,
    # )
    # AboutLi3 = models.CharField(
    #     verbose_name='Изменить текст пункта второго сектора 3',
    #     max_length=150,
    #     blank=True,
    #     null=True,
    # )
    AboutButton = models.CharField(
        verbose_name='Изменить текст кнопки второго сектора',
        max_length=150,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.AboutButton


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
    # AboutVideoSectionH3 = models.CharField(
    #     verbose_name='Изменить заговолок',
    #     max_length=150,
    #     blank=True,
    #     null=True,
    # )
    AboutVideoSectionP = models.TextField(
        verbose_name='Текст под заговолком',
        blank=True,
        null=True
    )
    # AboutVideoSectionLi1 = models.CharField(
    #     verbose_name='Изменить текст пункта 1',
    #     max_length=150,
    #     blank=True,
    #     null=True,
    # )
    # AboutVideoSectionLi2 = models.CharField(
    #     verbose_name='Изменить текст пункта 2',
    #     max_length=150,
    #     blank=True,
    #     null=True,
    # )
    # AboutVideoSectionLi3 = models.CharField(
    #     verbose_name='Изменить текст пункта 3',
    #     max_length=150,
    #     blank=True,
    #     null=True,
    # )
    # AboutVideoSectionLi4 = models.CharField(
    #     verbose_name='Изменить текст пункта 4',
    #     max_length=150,
    #     blank=True,
    #     null=True,
    # )
    # AboutVideoSectionEndP = models.TextField(
    #     verbose_name='Изменить текст в конце секции',
    #     blank=True,
    #     null=True
    # )

    def __str__(self):
        return 'обьект {}'.format(self.pk,)


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


class TestimonialsAndSevicesText(models.Model):
    TestimonialsH3 = models.CharField(
        verbose_name='Изменить заговолок секции Testimonials',
        max_length=150,
        blank=True,
        null=True,
    )
    TestimonialsP = models.TextField(
        verbose_name='Изменить текст под заговолком Testimonials',
        blank=True,
        null=True,
    )
    SevicesH3 = models.CharField(
        verbose_name='Изменить заговолок секции Sevices',
        max_length=150,
        blank=True,
        null=True,
    )
    SevicesP = models.TextField(
        verbose_name='Изменить текст под заговолком Sevices',
        blank=True,
        null=True,
    )
    SevicesCardBlockTitle1 = models.CharField(
        verbose_name='Изменить название первого карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    SevicesCardBlockText1 = models.TextField(
        verbose_name='Изменить текст первого карт блока',
        blank=True,
        null=True,
    )
    SevicesCardBlockTitle2 = models.CharField(
        verbose_name='Изменить название второго карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    SevicesCardBlockText2 = models.TextField(
        verbose_name='Изменить текст второго карт блока',
        blank=True,
        null=True,
    )
    SevicesCardBlockTitle3 = models.CharField(
        verbose_name='Изменить название третьего карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    SevicesCardBlockText3 = models.TextField(
        verbose_name='Изменить текст третьего карт блока',
        blank=True,
        null=True,
    )
    SevicesCardBlockTitle4 = models.CharField(
        verbose_name='Изменить название четвертого карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    SevicesCardBlockText4 = models.TextField(
        verbose_name='Изменить текст четвертого карт блока',
        blank=True,
        null=True,
    )
    SevicesCardBlockTitle5 = models.CharField(
        verbose_name='Изменить название пятого карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    SevicesCardBlockText5 = models.TextField(
        verbose_name='Изменить текст пятого карт блока',
        blank=True,
        null=True,
    )
    SevicesCardBlockTitle6 = models.CharField(
        verbose_name='Изменить название шестого карт блока',
        max_length=150,
        blank=True,
        null=True,
    )
    SevicesCardBlockText6 = models.TextField(
        verbose_name='Изменить текст шестого карт блока',
        blank=True,
        null=True,
    )

    def __str__(self):
        return '%s %s' % (
            self.TestimonialsH3,
            self.SevicesH3
        )


class CtaSection(models.Model):
    CtaH3 = models.CharField(
        verbose_name='Изменить текст заголовка',
        max_length=150,
        blank=True,
        null=True,
    )
    CtaP = models.TextField(
        verbose_name='Изменить текст блока',
        blank=True,
        null=True,
    )
    CtaBtn = models.CharField(
        verbose_name='Изменить текст кнопки',
        max_length=150,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.CtaH3


class Jobcategory(models.Model):
    JobCategoryName = models.CharField(
        verbose_name='Имя категории',
        max_length=150,
    )
    urs = models.SlugField(
        verbose_name='Ссылка категории',
        max_length=400,
        unique=True,
    )

    def __str__(self):
        return self.JobCategoryName


class JobText(models.Model):
    JobTextH3 = models.CharField(
        verbose_name='Изменить заговолок',
        max_length=150,
        blank=True,
        null=True,
    )
    JobTextP = models.TextField(
        verbose_name='Текст под заговолком',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.JobTextH3


class MyJob(models.Model):
    MyJobProductTitle = models.CharField(
        verbose_name='Название продукта',
        default='продукт',
        max_length=150,
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        verbose_name='Ссылка на работу',
        max_length=200,
        default='TextTitle',
        help_text='Ссылка создается автоматически из названия продукта',
        unique=True
    )
    CheckLink = models.BooleanField(
        verbose_name='Поставьте эту галочку, если хотите добавить ссыльку на работу на внешнем сайте',
        default=False,
    )
    ExternalLink = models.CharField(
        verbose_name='Внешная ссылька на работу',
        max_length=250,
        blank=True,
        null=True,
    )
    MyJobJobCategoryTitle = models.CharField(
        verbose_name='Название пункта категория',
        default='категория',
        max_length=150,
        blank=True,
        null=True,
    )
    MyJobUrlTitle = models.CharField(
        verbose_name='Изменить название пункта ссылка на продукт',
        default='ссылка на продукт',
        max_length=150,
        blank=True,
        null=True,
    )    
    MyJobJobCategory = models.ForeignKey(
        Jobcategory,
        on_delete=models.PROTECT,
        verbose_name='Выберите категорию',
    )
    MyJobClientTitle = models.CharField(
        verbose_name='Названия пункта клиент',
        default=' клиент',
        max_length=200,
        blank=True,
        null=True,
    )
    MyJobClient = models.CharField(
        verbose_name='Имя или названия клиента',
        max_length=200,
        blank=True,
        null=True,
    )
    MyJobDateTitle = models.CharField(
        verbose_name='Названия пункта дата создания',
        default='дата создания',
        max_length=200,
        blank=True,
        null=True,
    )
    MyJobDate = models.DateField(
        verbose_name='дата создания проекта',
        default=date.today,
        unique=False,
        unique_for_date=False,
    )
    MyJobH2 = models.CharField(
        verbose_name='Заглавие продукта',
        max_length=150,
        blank=True,
        null=True
    )
    MyJobDescription = models.TextField(
        verbose_name='описание продукта',
        blank=True,
        null=True,
    )
    MyJobImage1 = models.ImageField(
        verbose_name='Загрузить главную картинки',
        upload_to='More'
    )
    MyJobImage2 = models.ImageField(
        verbose_name='Загрузить вторую картинки',
        upload_to='More'
    )
    MyJobImage3 = models.ImageField(
        verbose_name='Загрузить третью картинки',
        upload_to='More'
    )
    MyJobUrlTitle = models.CharField(
        verbose_name='Изменить название пункта ссылка на продукт',
        default='ссылка на продукт',
        max_length=150,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse('CardApp:MyJobView', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = translit.slugify(self.MyJobProductTitle)
        super(MyJob, self).save(*args, **kwargs)

    def __str__(self):
        return self.MyJobProductTitle


class pricing(models.Model):
    CurrencyList = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
    )
    PricingH3 = models.CharField(
        verbose_name='Изменить текст заголовка',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingP = models.TextField(
        verbose_name='Изменить текст блока',
        blank=True,
        null=True,
    )
    PricingTitleColumn1 = models.CharField(
        verbose_name='Изменить название первой колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCurrencyColumn1 = models.CharField(
        verbose_name='Изменить валюту первой колонки',
        max_length=150,
        choices=CurrencyList,
        blank=True,
        null=True,
    )
    PricingPriceColumn1 = models.DecimalField(
        verbose_name='Изменить цену первой колонки',
        max_digits=10,
        decimal_places=2,
        null=True,
    )
    PricingPriceColumn1 = models.DecimalField(
        verbose_name='Изменить цену первой колонки',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    PricingMonthColumn1 = models.CharField(
        verbose_name='Изменить текст после цены первой колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingUl1Li1 = models.CharField(
        verbose_name='Изменить текст первого пункта первой колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl1Li1 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl1Li2 = models.CharField(
        verbose_name='Изменить текст второго пункта первой колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl1Li2 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl1Li3 = models.CharField(
        verbose_name='Изменить текст третьего пункта первой колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl1Li3 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl1Li4 = models.CharField(
        verbose_name='Изменить текст четвертого пункта первой колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl1Li4 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl1Li5 = models.CharField(
        verbose_name='Изменить текст пятого пункта первой колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl1Li5 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl1bBtn = models.CharField(
        verbose_name='Изменить текст кнопки первой колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingTitleColumn2 = models.CharField(
        verbose_name='Изменить название второй колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCurrencyColumn2 = models.CharField(
        verbose_name='Изменить валюту второй колонки',
        max_length=150,
        choices=CurrencyList,
        blank=True,
        null=True,
    )
    PricingPriceColumn2 = models.DecimalField(
        verbose_name='Изменить цену второй колонки',
        max_digits=10,
        decimal_places=2,
        null=True,
    )
    PricingPriceColumn2 = models.DecimalField(
        verbose_name='Изменить цену второй колонки',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    PricingMonthColumn2 = models.CharField(
        verbose_name='Изменить текст после цены второй колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingUl2Li1 = models.CharField(
        verbose_name='Изменить текст первого пункта второй колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl2Li1 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl2Li2 = models.CharField(
        verbose_name='Изменить текст второго пункта второй колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl2Li2 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl2Li3 = models.CharField(
        verbose_name='Изменить текст третьего пункта второй колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl2Li3 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl2Li4 = models.CharField(
        verbose_name='Изменить текст четвертого пункта второй колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl2Li4 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl2Li5 = models.CharField(
        verbose_name='Изменить текст пятого пункта второй колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl2Li5 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl1bBtn2 = models.CharField(
        verbose_name='Изменить текст кнопки второй колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingTitleColumn3 = models.CharField(
        verbose_name='Изменить название третий колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCurrencyColumn3 = models.CharField(
        verbose_name='Изменить валюту третий колонки',
        max_length=150,
        choices=CurrencyList,
        blank=True,
        null=True,
    )
    PricingPriceColumn3 = models.DecimalField(
        verbose_name='Изменить цену третий колонки',
        max_digits=10,
        decimal_places=2,
        null=True,
    )
    PricingPriceColumn3 = models.DecimalField(
        verbose_name='Изменить цену третий колонки',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    PricingMonthColumn3 = models.CharField(
        verbose_name='Изменить текст после цены третий колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingUl3Li1 = models.CharField(
        verbose_name='Изменить текст первого пункта третий колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl3Li1 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl3Li2 = models.CharField(
        verbose_name='Изменить текст второго пункта третий колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl3Li2 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl3Li3 = models.CharField(
        verbose_name='Изменить текст третьего пункта третий колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl3Li3 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl3Li4 = models.CharField(
        verbose_name='Изменить текст четвертого пункта третий колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl3Li4 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl3Li5 = models.CharField(
        verbose_name='Изменить текст пятого пункта третий колонки',
        max_length=150,
        blank=True,
        null=True,
    )
    PricingCheckUl3Li5 = models.BooleanField(
        verbose_name='Включить пункт',
        default=True,
    )
    PricingUl1bBtn3 = models.CharField(
        verbose_name='Изменить текст кнопки третий колонки',
        max_length=150,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.PricingH3


class TeamText(models.Model):
    TeamTextH3 = models.CharField(
        verbose_name='Изменить заговолок',
        max_length=150,
        blank=True,
        null=True,
    )
    TeamTextP = models.TextField(
        verbose_name='Текст под заговолком',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.TeamTextH3


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


class QuestionsSectionText(models.Model):
    QuestionsSectionTextH3 = models.CharField(
        verbose_name='Изменить текст заголовка',
        max_length=150,
        blank=True,
        null=True,
    )
    QuestionsSectionTextP = models.TextField(
        verbose_name='Изменить текст блока',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.QuestionsSectionTextH3


class GenericAsk(models.Model):
    GenericAskLi = models.CharField(
        verbose_name='Изменить текст вопроса',
        max_length=150,
        blank=True,
        null=True,
    )
    GenericAskP = models.TextField(
        verbose_name='Изменить текст ответа',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.GenericAskLi


class contact(models.Model):
    ContactH3 = models.CharField(
        verbose_name='Изменить заговолок',
        max_length=150,
        blank=True,
        null=True,
    )
    ContactP = models.TextField(
        verbose_name='Текст под заговолком',
        blank=True,
        null=True
    )
    LocationTitle = models.CharField(
        verbose_name='Изменить название пункта локакция',
        max_length=150,
        blank=True,
        null=True,
    )
    location = models.CharField(
        verbose_name='Изменить локакцию',
        max_length=150,
        blank=True,
        null=True,
    )
    EmailTitle = models.CharField(
        verbose_name='Изменить название пункта почта',
        max_length=150,
        blank=True,
        null=True,
    )
    Email = models.EmailField(
        verbose_name='Ваша почта',
        max_length=254,
    )
    CallTitle = models.CharField(
        verbose_name='Изменить название пункта телефон',
        max_length=150,
        blank=True,
        null=True,
    )
    call = models.CharField(
        verbose_name='Ваш телефон',
        max_length=150,
        blank=True,
        null=True,
    )

    def __str__(self):
        return 'почта {} телефон {}'.format(self.Email, self.call)

class SocNet(models.Model):
    SocChoice = (
        ('adobe', 'adobe'),
        ('airbnb', 'airbnb'),
        ('algolia', 'algolia'),
        ('amazon', 'amazon'),
        ('android', 'android'),
        ('angular', 'angular'),
        ('apple', 'apple'),
        ('audible', 'audible'),
        ('baidu', 'baidu'),
        ('behance', 'behance'),
        ('bing', 'bing'),
        ('bitcoin', 'bitcoin'),
        ('blogger', 'blogger'),
        ('bootstrap', 'bootstrap'),
        ('chrome', 'chrome'),
        ('codepen', 'codepen'),
        ('creative-commons', 'creative-commons'),
        ('css3', 'css3'),
        ('dailymotion', 'dailymotion'),
        ('deviantart', 'deviantart'),
        ('dev-to', 'dev-to'),
        ('digg', 'digg'),
        ('digitalocean', 'digitalocean'),
        ('discord', 'discord'),
        ('discourse', 'discourse'),
        ('dribbble', 'dribbble'),
        ('dropbox', 'dropbox'),
        ('drupal', 'drupal'),
        ('ebay', 'ebay'),
        ('edge', 'edge'),
        ('etsy', 'etsy'),
        ('facebook', 'facebook'),
        ('figma', 'figma'),
        ('firefox', 'firefox'),
        ('flickr', 'flickr'),
        ('foursquare', 'foursquare'),
        ('git', 'git'),
        ('github', 'github'),
        ('gitlab', 'gitlab'),
        ('google', 'google'),
        ('imdb', 'imdb'),
        ('instagram', 'instagram'),
        ('internet-explorer', 'internet-explorer'),
        ('invision', 'invision'),
        ('javascript', 'javascript'),
        ('joomla', 'joomla'),
        ('jquery', 'jquery'),
        ('jsfiddle', 'jsfiddle'),
        ('kickstarter', 'kickstarter'),
        ('less', 'less'),
        ('linkedin', 'linkedin'),
        ('magento', 'magento'),
        ('mailchimp', 'mailchimp'),
        ('mastercard', 'mastercard'),
        ('medium', 'medium'),
        ('medium-old', 'medium-old'),
        ('messenger', 'messenger'),
        ('microsoft', 'microsoft'),
        ('nodejs', 'nodejs'),
        ('opera', 'opera'),
        ('patreon', 'patreon'),
        ('paypal', 'paypal'),
        ('periscope', 'periscope'),
        ('pinterest', 'pinterest'),
        ('play-play', 'play-play'),
        ('pocket', 'pocket'),
        ('product-hunt', 'product-hunt'),
        ('quora', 'quora'),
        ('react', 'react'),
        ('redbubble', 'redbubble'),
        ('reddit', 'reddit'),
        ('redux', 'redux'),
        ('sass', 'sass'),
        ('shopify', 'shopify'),
        ('skype', 'skype'),
        ('slack', 'slack'),
        ('snapchat', 'snapchat'),
        ('soundcloud', 'soundcloud'),
        ('spotify', 'spotify'),
        ('squarespace', 'squarespace'),
        ('stack', 'stack'),
        ('stripe', 'stripe'),
        ('telegram', 'telegram'),
        ('trello', 'trello'),
        ('tumblr', 'tumblr'),
        ('twitch', 'twitch'),
        ('twitter', 'twitter'),
        ('unsplash', 'unsplash'),
        ('vimeo', 'vimeo'),
        ('visa', 'visa'),
        ('vk', 'vk'),
        ('vuejs', 'vuejs'),
        ('whatsapp', 'whatsapp'),
        ('wikipedia', 'wikipedia'),
        ('windows', 'windows'),
        ('wix', 'wix'),
        ('wordpress', 'wordpress'),
        ('yahoo', 'yahoo'),
        ('yelp', 'yelp'),
        ('youtube', 'youtube'),
    )

    SocIcon = models.CharField(
        verbose_name='выберите соц.сеть либо иконку из списка',
        max_length=250,
        choices=SocChoice
    )
    SocUrl = models.URLField(
        verbose_name='Введите ссылку',
        max_length=200
    )

    def __str__(self):
        return 'ссылка на {}'.format(self.SocUrl)
