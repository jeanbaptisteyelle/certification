from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Travel
        fields = '__all__'

class FashionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fashion
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categorie
        fields = '__all__'



