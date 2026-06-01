from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home_fun),
    path('about/', views.about_fun),
    path('contact/', views.contact_fun),
]