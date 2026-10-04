from django.contrib import admin
from django.urls import path
from myapp.views import hello
from . import views

urlpatterns = [
    path('', hello),
    path('about/', views.about)

]