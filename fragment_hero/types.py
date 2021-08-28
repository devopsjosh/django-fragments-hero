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

    def resolve_background_image(self, info):
        if self.background_image:
            return info.context.build_absolute_uri(self.background_image.url)
        return None

    def resolve_foreground_image(self, info):
        if self.foreground_image:
            return info.context.build_absolute_uri(self.foreground_image.url)
        return None


class HeroCallToActionNode(DjangoObjectType):
    class Meta:
        model = HeroCallToAction

        filter_fields = {
            'hero': ['exact'],
        }
        interfaces = (relay.Node,)
