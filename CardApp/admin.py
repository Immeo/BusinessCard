from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


# Register your models here.
class logoForm(forms.ModelForm):
    """
    docstring
    """
    logotype = forms.CharField(
        label='Ваше Лого', widget=CKEditorUploadingWidget())

    class Meta:
        model = logo
        fields = '__all__'


class logoAdmin(admin.ModelAdmin):
    form = logoForm


admin.site.register(logo, logoAdmin)
admin.site.register(nav)
admin.site.register(hero)


class AboutSectionForm(forms.ModelForm):
    """
    docstring
    """
    AboutSectionP = forms.CharField(
        label='Текст под заговолком', widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutSection
        fields = '__all__'


class AboutSectionAdmin(admin.ModelAdmin):
    form = AboutSectionForm

admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(CountsSection)

class AboutVideoSectionForm(forms.ModelForm):
    """
    docstring
    """
    AboutVideoSectionP = forms.CharField(label='Текст под заговолком', widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutVideoSection
        fields = '__all__'

class AboutVideoSectionAdmin(admin.ModelAdmin):
    form = AboutVideoSectionForm


admin.site.register(AboutVideoSection, AboutVideoSectionAdmin)
admin.site.register(reviews)


class TestimonialsAndSevicesTextForm(forms.ModelForm):
    """
    docstring
    """
    TestimonialsP = forms.CharField(
        label='Текст под заговолком', widget=CKEditorUploadingWidget())
    SevicesP = forms.CharField(
        label='Текст под заговолком', widget=CKEditorUploadingWidget())

    class Meta:
        model = TestimonialsAndSevicesText
        fields = '__all__'


class TestimonialsAndSevicesTextAdmin(admin.ModelAdmin):
    form = TestimonialsAndSevicesTextForm


admin.site.register(TestimonialsAndSevicesText, TestimonialsAndSevicesTextAdmin)


class CtaSectionForm(forms.ModelForm):
    """
    docstring
    """
    CtaP = forms.CharField(
        label='Текст под заговолком', widget=CKEditorUploadingWidget())

    class Meta:
        model = CtaSection
        fields = '__all__'


class CtaSectionAdmin(admin.ModelAdmin):
    form = CtaSectionForm


admin.site.register(CtaSection, CtaSectionAdmin)

admin.site.register(pricing)
admin.site.register(TeamText)
admin.site.register(team)
admin.site.register(QuestionsSectionText)
admin.site.register(GenericAsk)


class JobTextForm(forms.ModelForm):
    """
    docstring
    """
    JobTextP = forms.CharField(
        label='Текст под заговолком', widget=CKEditorUploadingWidget())

    class Meta:
        model = JobText
        fields = '__all__'


class JobTextAdmin(admin.ModelAdmin):
    form = JobTextForm


admin.site.register(JobText, JobTextAdmin)
admin.site.register(Jobcategory)


class MyJobForm(forms.ModelForm):
    """
    docstring
    """
    MyJobDescription = forms.CharField(
        label='Текст под заговолком', widget=CKEditorUploadingWidget())

    class Meta:
        model = MyJob
        fields = '__all__'


class MyJobAdmin(admin.ModelAdmin):
    form = MyJobForm


admin.site.register(MyJob, MyJobAdmin)
admin.site.register(contact)
admin.site.register(SocNet)
