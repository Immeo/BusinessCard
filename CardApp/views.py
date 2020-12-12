from django.views.generic import ListView, DetailView
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
        context['Jobcategory'] = Jobcategory.objects.all()
        context['MyJob'] = MyJob.objects.all()
        return context


class MyJobView(DetailView):
    model = MyJob
    template_name = 'CardApp/portfolio-details.html'

    def get_context_data(self, **kwargs):
        context = super(MyJobView, self).get_context_data(**kwargs)
        context['Jobcategory'] = Jobcategory.objects.all()
        context['nav'] = nav.objects.all()
        return context
