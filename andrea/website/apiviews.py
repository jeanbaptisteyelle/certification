from . import serializers, models
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from . import models


class Contact(generics.ListCreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    def post(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        contact = models.Contact.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff:
            raise PermissionDenied("You can not create a Contact.")
        return super().post(request, *args, **kwargs)


class InfoContactViewSet(viewsets.ModelViewSet):
    queryset = models.InfoContact.objects.all()
    serializer_class = serializers.InfoContactSerializer
    def destroy(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        reseau = models.InfoContact.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff :
            raise PermissionDenied("You can not delete this Info Contact.")
        return super().destroy(request, *args, **kwargs)


class Newletter(generics.ListCreateAPIView):
    queryset = models.Newletter.objects.all()
    serializer_class = serializers.NewletterSerializer
    def post(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        Newletter = models.Newletter.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff:
            raise PermissionDenied("You can not create a Newletter.")
        return super().post(request, *args, **kwargs)


class SiteinfoViewSet(viewsets.ModelViewSet):
    queryset = models.Siteinfo.objects.all()
    serializer_class = serializers.SiteinfoSerializer
    def destroy(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        reseau = models.Siteinfo.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff :
            raise PermissionDenied("You can not delete this Info Siteinfo.")
        return super().destroy(request, *args, **kwargs)

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.Userserializer

class Login(APIView):
    permission_classes = ()
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': "Mauvaises informations d'identification"}, status=status.HTTP_404_BAD_REQUEST)
