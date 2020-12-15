from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from BusinessCard.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import SendForm
from .models import *
# Create your views here.


class navListView(ListView):
    model = nav
    template_name = "CardApp/index.html"
    context_object_name = 'nav'

    def get_context_data(self, **kwargs):
        context = super(navListView, self).get_context_data(**kwargs)
        context['hero'] = hero.objects.all()
        context['reviews'] = reviews.objects.all()
        context['AboutSection'] = AboutSection.objects.all()
        context['CountsSection'] = CountsSection.objects.all()
        context['AboutVideoSection'] = AboutVideoSection.objects.all()
        context['TestimonialsAndSevicesText'] = TestimonialsAndSevicesText.objects.all()
        context['CtaSection'] = CtaSection.objects.all()
        context['pricing'] = pricing.objects.all()
        context['team'] = team.objects.all()
        context['QuestionsSectionText'] = QuestionsSectionText.objects.all()
        context['GenericAsk'] = GenericAsk.objects.all()
        context['TeamText'] = TeamText.objects.all()
        context['JobText'] = JobText.objects.all()
        context['Jobcategory'] = Jobcategory.objects.all()
        context['MyJob'] = MyJob.objects.all()
        context['contact'] = contact.objects.all()
        context['SendForm'] = SendForm()
        return context


class SendFormView(FormView):

    form_class = SendForm
    template_name = "CardApp/email_form.html"
    context_object_name = 'SendForm'
    success_url = 's'

# this is what you want
    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='evgenvolk158@gmail.com',
            recipient_list=["evgenvolk158@gmail.com"],
            fail_silently=False,
        )
        return super(SendFormView, self).form_valid(form)


class MyJobView(DetailView):
    model = MyJob
    template_name = 'CardApp/portfolio-details.html'

    def get_context_data(self, **kwargs):
        context = super(MyJobView, self).get_context_data(**kwargs)
        context['Jobcategory'] = Jobcategory.objects.all()
        context['nav'] = nav.objects.all()
        return context
