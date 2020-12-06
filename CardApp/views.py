# from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.


class TopNavAndHeroListView(ListView):
    model = TopNavAndHero
    template_name = "CardApp/index.html"

    def get_context_data(self, **kwargs):
        context = super(TopNavAndHeroListView, self).get_context_data(**kwargs)
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
        return context
