from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from . import models

class CategorieNode(DjangoObjectType):
    class Meta:
        model = models.Categorie
        filter_fields = ['nom',]
        interfaces = (relay.Node, )


class TagNode(DjangoObjectType):
    class Meta:
        model = models.Tag
        filter_fields = ['nom',]
        interfaces = (relay.Node, )

class FashionNode(DjangoObjectType):
    class Meta:
        model = models.Fashion
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'categorie': ['exact'],
            'tag': ['exact'],
            'content': ['exact'],
            'created_by': ['exact'],
        }
        interfaces = (relay.Node, )

class TravelNode(DjangoObjectType):
    class Meta:
        model = models.Travel
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'categorie': ['exact'],
            'tag': ['exact'],
            'content': ['exact'],
            'created_by': ['exact'],
        }
        interfaces = (relay.Node, )

class AboutNode(DjangoObjectType):
    class Meta:
        model = models.About
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact',],

        }
        interfaces = (relay.Node, )

class Query(object):
    categorie = relay.Node.Field(CategorieNode)
    all_categories = DjangoFilterConnectionField(CategorieNode)

    tag = relay.Node.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TagNode)
   
    fashion = relay.Node.Field(FashionNode)
    all_fashions = DjangoFilterConnectionField(FashionNode)
    
    travel = relay.Node.Field(TravelNode)
    all_travels = DjangoFilterConnectionField(TravelNode)
    
    about = relay.Node.Field(AboutNode)
    all_abouts = DjangoFilterConnectionField(AboutNode)
    
    
    

   