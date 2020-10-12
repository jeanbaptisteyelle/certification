from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from . import models

class SiteinfoNode(DjangoObjectType):
    class Meta:
        model = models.Siteinfo
        filter_fields = {
            'logo': ['exact',],
            'copyrights': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class NewletterNode(DjangoObjectType):
    class Meta:
        model = models.Newletter
        filter_fields = {
            'email': ['exact'],
        }
        interfaces = (relay.Node, )


class InfoContactNode(DjangoObjectType):
    class Meta:
        model = models.InfoContact
        filter_fields = {
            'address': ['exact', 'icontains', 'istartswith'],
            'phone': ['exact', 'icontains', 'istartswith'],
            'email': ['exact'],
            'website': ['exact'],
            'marp_url': ['exact'],
        }
        interfaces = (relay.Node, )

class ContactNode(DjangoObjectType):
    class Meta:
        model = models.Contact
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'email': ['exact',],
            'subject': ['exact','icontains', 'istartswith'],
            'message': ['exact','icontains', 'istartswith'],
           
        }
        interfaces = (relay.Node, )

class Query(object):
    Siteinfo = relay.Node.Field(SiteinfoNode)
    all_Siteinfo = DjangoFilterConnectionField(SiteinfoNode)

    newletter = relay.Node.Field(NewletterNode)
    all_newletter = DjangoFilterConnectionField(NewletterNode)
   
    infoContact = relay.Node.Field(InfoContactNode)
    all_fashion = DjangoFilterConnectionField(InfoContactNode)
    
    Contact = relay.Node.Field(ContactNode)
    all_travel = DjangoFilterConnectionField(ContactNode)


