
from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.authtoken import views
from . import apiviews, views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('infocontact', apiviews.InfoContactViewSet, basename='infocontact-api')
router.register('siteinfo', apiviews.SiteinfoViewSet, basename='siteinfo-api')
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('newletter', views.newletter, name='newletter'),
    #Routes Api
    path('contacts', apiviews.Contact.as_view(), name='Contacts'),
    path('newletters', apiviews.Newletter.as_view(), name='newletters'),
    path('login', apiviews.Login.as_view(), name='login'),
    path('users', apiviews.UserCreate.as_view(), name='user_create'),

    path("api/", include(router.urls))
<<<<<<< HEAD
=======

>>>>>>> parent of 3a480ee... correction des api
]
