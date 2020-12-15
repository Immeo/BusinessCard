from django.urls import path
from .views import navListView, MyJobView, SendFormView

app_name = 'CardApp'

urlpatterns = [
    path('', navListView.as_view(), name='home'),
    path('job/<slug:slug>/', MyJobView.as_view(), name='MyJobView'),
    path('s', SendFormView.as_view(), name='send')
]
