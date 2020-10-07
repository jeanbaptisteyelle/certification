from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'
class InfoContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InfoContact
        fields = '__all__'
class NewletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Newletter
        fields = '__all__'

class SiteinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Siteinfo
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only':True}}
    def create(self, validated_data):
        user=User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
           
