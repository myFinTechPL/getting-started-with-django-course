# Alexandria/home/urls.py

from django.urls import path

from home import views

urlpatterns = [
    path('sample/', views.sample),
    path('sample_my/', views.sample_my),
    path('about/', views.about),
]
