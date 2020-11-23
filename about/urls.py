from . import views
from django.urls import path
from django.conf import settings

app_name = 'about'

urlpatterns = [
    path('', views.about, name="about"),
]