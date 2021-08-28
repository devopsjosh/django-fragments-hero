from graphene_django import DjangoObjectType
from graphene import relay

from fragment_hero.models import Hero, HeroCallToAction
import graphene


class HeroNode(DjangoObjectType):
    is_active = graphene.Boolean()

    class Meta:
        model = Hero

        filter_fields = {
            'name': ['exact', 'icontains'],
        }
        interfaces = (relay.Node,)

    def resolve_is_active(self, info):
        return self.is_active


class HeroCallToActionNode(DjangoObjectType):
    class Meta:
        model = HeroCallToAction

        filter_fields = {
            'hero': ['exact'],
        }
        interfaces = (relay.Node,)
