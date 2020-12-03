# from django.shortcuts import render
from django.views.generic import ListView
from .models import EditTtext, reviews, team
# Create your views here.


class EditTtextListView(ListView):
    model = EditTtext
    template_name = "CardApp/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(EditTtextListView, self).get_context_data(**kwargs)
        context['reviews'] = reviews.objects.all()
        context['team'] = team.objects.all()
        return context
    
