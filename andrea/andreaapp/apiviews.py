from . import serializers, models
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.exceptions import PermissionDenied
from . import models

class About(generics.ListCreateAPIView):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer
    def post(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        info = models.About.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff:
            raise PermissionDenied("You can not create a about.")
        return super().post(request, *args, **kwargs)


class TravelViewSet(viewsets.ModelViewSet):
    queryset = models.Travel.objects.all()
    serializer_class = serializers.TravelSerializer
    def destroy(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        reseau = models.Travel.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff :
            raise PermissionDenied("You can not delete this reseaux sociaux.")
        return super().destroy(request, *args, **kwargs)


class FashionViewSet(viewsets.ModelViewSet):
    queryset = models.Fashion.objects.all()
    serializer_class = serializers.FashionSerializer
    def destroy(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        reseau = models.Travel.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff :
            raise PermissionDenied("You can not delete this Fashion.")
        return super().destroy(request, *args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    def destroy(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        reseau = models.Tag.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff :
            raise PermissionDenied("You can not delete this Tag.")
        return super().destroy(request, *args, **kwargs)


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = models.Categorie.objects.all()
    serializer_class = serializers.CategorieSerializer
    def destroy(self, request, *args, **kwargs):
        user = request.POST.get('username')
        users = User.objects.filter(username=user)
        if not users.count() == 1:
            datas = {'success': False, 'message': 'username is not correct'}
            return JsonResponse(datas)
        else:
            user = users.first()
        reseau = models.Categorie.objects.get(pk=self.kwargs["pk"])
        if not user.is_staff :
            raise PermissionDenied("You can not delete this reseaux sociaux.")
        return super().destroy(request, *args, **kwargs)

