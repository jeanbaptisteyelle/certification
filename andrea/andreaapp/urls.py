from django.urls import path
from . import views
urlpatterns = [
    path('', views.fashion, name='fashion'),
    path('travel', views.travel, name='travel'),
    path('about', views.about, name='about'),
    path('single', views.single, name='single'),
    

]
