from django.contrib import admin
from fragment_hero.models import Hero, HeroCallToAction


class HeroCallToActionInline(admin.StackedInline):
    model = HeroCallToAction
    extra = 1


class HeroAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        '__str__', 'name', 'start', 'end', 'is_active'
    ]
    list_filter = ('start', 'end',)
    inlines = [HeroCallToActionInline, ]


admin.site.register(Hero, HeroAdmin)
