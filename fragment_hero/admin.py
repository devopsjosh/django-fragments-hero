from django.contrib import admin
from .models import Category, Hierarchy
from fragment_hero.models import Hero, HeroCallToAction


class HeroAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        '__str__', 'name', 'start', 'end', 'is_active'
    ]
    list_filter = ('start', 'end', 'is_active')


class HeroCallToActionAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'hero']
    list_filter = ('hero',)


admin.site.register(Hero, HeroAdmin)
admin.site.register(HeroCallToAction, HeroCallToActionAdmin)
