# from django.shortcuts import render
from django.views.generic import ListView
from .models import edit_text
# Create your views here.


class edit_textListView(ListView):
    model = edit_text
    template_name = "CardApp/index.html"