from graphene_django import DjangoObjectType
from graphene import relay

from fragment_hero.models import Hero, HeroCallToAction


class HeroNode(DjangoObjectType):
    class Meta:
        model = Hero

        filter_fields = {
            'name': ['exact', 'icontains'],
            'is_active': ['exact', ]
        }
        interfaces = (relay.Node,)


class HeroCallToActionNode(DjangoObjectType):
    class Meta:
        model = HeroCallToAction

        filter_fields = {
            'hero': ['exact'],
        }
        interfaces = (relay.Node,)
