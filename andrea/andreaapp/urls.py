<<<<<<< HEAD
from django.urls import path
from . import views

=======
>>>>>>> parent of 291c4f7... commit heroku
from django.urls import path, include
from rest_framework.authtoken import views
from . import apiviews, views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('travels', apiviews.TravelViewSet, basename='travel-api'),
router.register('fashions', apiviews.FashionViewSet, basename='fashion-api')
router.register('tags', apiviews.TagViewSet, basename='fashion-api')
router.register('categorie', apiviews.CategorieViewSet, basename='fashion-api')

<<<<<<< HEAD
=======

>>>>>>> parent of 291c4f7... commit heroku
urlpatterns = [

    path('', views.fashion, name='fashion'),
    path('travel', views.travel, name='travel'),
    path('about', views.about, name='about'),
<<<<<<< HEAD
    path('single', views.single, name='single'),
    

=======
>>>>>>> parent of 291c4f7... commit heroku
    path('single/<slug>', views.single, name='single'),
    path('single/', views.single, name='single'),

    # vues api
    path('about/<int:pk>', apiviews.About.as_view(), name='about'),
    path("api/", include(router.urls)),
<<<<<<< HEAD

=======
>>>>>>> parent of 291c4f7... commit heroku
]
