from django.urls import path
from .views import navListView, MyJobView

app_name = 'CardApp'

urlpatterns = [
    path('', navListView.as_view(), name='home'),
    path('job/<slug:slug>/', MyJobView.as_view(), name='MyJobView')
]
