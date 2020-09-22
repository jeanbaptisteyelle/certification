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
            'image': ['exact', 'icontains', 'istartswith'],
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'categorie': ['exact'],
            'content': ['exact'],
            'created_by': ['exact'],
        }
        interfaces = (relay.Node, )

class Travel(DjangoObjectType):
    class Meta:
        model = models.Travel
        filter_fields = {
            'image': ['exact', 'icontains', 'istartswith'],
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact'],
        }
        interfaces = (relay.Node, )

class About(DjangoObjectType):
    class Meta:
        model = models.About
        filter_fields = {
            'background': ['exact', 'icontains', 'istartswith'],
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class Query(object):
    categorie = relay.Node.Field(CategorieNode)
    all_categories = DjangoFilterConnectionField(CategorieNode)

    tag = relay.Node.Field(TagNode)
    all_tag = DjangoFilterConnectionField(TagNode)
   
    fashion = relay.Node.Field(FashionNode)
    all_fashion = DjangoFilterConnectionField(FashionNode)
    
    travel = relay.Node.Field(TravelNode)
    all_travel = DjangoFilterConnectionField(TravelNode)

    about = relay.Node.Field(AboutNode)
    all_about = DjangoFilterConnectionField(AboutNode)


   