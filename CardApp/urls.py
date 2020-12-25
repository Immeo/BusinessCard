from django.urls import path
from .views import navListView, MyJobView, EmailAttachementView

app_name = 'CardApp'

urlpatterns = [
    path('', navListView.as_view(), name='home'),
    path('job/<slug:slug>/', MyJobView.as_view(), name='MyJobView'),
    path('send', EmailAttachementView.as_view(), name='emailattachment')
]
