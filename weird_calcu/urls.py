from django.urls import path
from . import views

urlpatterns = [
    path('calculated', views.calculated, name='weird_calculated'),
]
