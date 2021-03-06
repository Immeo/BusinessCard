from django.http import HttpResponseRedirect
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.core.mail import EmailMessage, send_mail
from BusinessCard.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import EmailForm, SubscribeForm
from .models import *
# Create your views here.


class navListView(ListView):
    method_decorator(csrf_exempt)
    model = nav
    template_name = "CardApp/index.html"
    context_object_name = 'nav'
    # form_class = SubscribeForm

    def get_context_data(self, **kwargs):
        context = super(navListView, self).get_context_data(**kwargs)
        context['logo'] = logo.objects.all()
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
        context['FooterListHeaders'] = FooterListHeaders.objects.all()
        context['FooterLinksTwo'] = FooterLinksTwo.objects.all()
        context['FooterSubscribeF'] = FooterSubscribeF.objects.all()
        context['SocNet'] = SocNet.objects.all()
        context['EmailForm'] = EmailForm()
        context['SubscribeForm'] = SubscribeForm()
        return context


class EmailAttachementView(View):
    method_decorator(csrf_exempt)
    form_class = EmailForm
    template_name = 'CardApp/email_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject'].strip()
            message = "{name} / {email} said: ".format(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'))
            message += "\n\n{0}".format(form.cleaned_data.get('message'))
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(
                    subject=subject, body=message, from_email=email, to=RECIPIENTS_EMAIL)
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'письмо отправлено на %s' % email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Файл слишком велик'})

            return render(request, self.template_name, {'email_form': form, 'error_message': 'возникла ошибка, попробуйте позже'})


def SubscribeFormViews(request):
    SUBJECT = "The message from a contact form"
    message = '''try'''
    if not request.is_ajax():
        raise Http404('No ajax!')
    else:
        form = SubscribeForm(request.POST or None)
        if form.is_valid():
            EMAIL_TO = form.cleaned_data['SubEemail']
            send_mail(SUBJECT, message, DEFAULT_FROM_EMAIL, [EMAIL_TO])
            # print(email_content)
            r = {'form_is_valid': True}
        else:
            r = {'form_is_valid': False, 'form_errors': form.errors.as_json()}
    return JsonResponse(r)

class MyJobView(DetailView):
    method_decorator(csrf_exempt)
    
    model = MyJob
    template_name = 'CardApp/portfolio-details.html'

    def get_context_data(self, **kwargs):
        context = super(MyJobView, self).get_context_data(**kwargs)
        context['logo'] = logo.objects.all()
        context['Jobcategory'] = Jobcategory.objects.all()
        context['nav'] = nav.objects.all()
        context['contact'] = contact.objects.all()
        context['SocNet'] = SocNet.objects.all()
        context['FooterListHeaders'] = FooterListHeaders.objects.all()
        context['FooterLinksTwo'] = FooterLinksTwo.objects.all()
        context['FooterSubscribeF'] = FooterSubscribeF.objects.all()
        context['SubscribeForm'] = SubscribeForm()
        return context
