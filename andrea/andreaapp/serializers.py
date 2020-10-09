from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = ('background','titre','description')


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Travel
        fields = ('image','titre','description')

class FashionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fashion
        fields = ('image','titre','description','categorie','tag','content','created_by')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = 'nom'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categorie
        fields = 'nom'



