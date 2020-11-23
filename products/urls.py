from . import views
from django.urls import path
from django.conf import settings


app_name = 'products'

urlpatterns = [
    path('', views.products, name="products"),
]