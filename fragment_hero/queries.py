import graphene
from graphene_django.filter import DjangoFilterConnectionField

from fragment_hero.types import HeroCallToActionNode, HeroNode


class Query(graphene.ObjectType):
    hero = graphene.relay.Node.Field(
        HeroNode, description="Queries a single hero.")
    heroes = DjangoFilterConnectionField(
        HeroNode, description="Queries a paginated list of heroes.")

    hero_call_to_action = graphene.relay.Node.Field(
        HeroCallToActionNode, description="Queries a single hero call to action.")
    hero_call_to_actions = DjangoFilterConnectionField(
        HeroCallToActionNode, description="Queries a paginated list of hero call to actions.")
