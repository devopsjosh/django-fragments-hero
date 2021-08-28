import re
import operator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext, gettext_lazy as _
import datetime


class Hero(models.Model):
    name = models.CharField(_("name"), max_length=255)
    background_image = models.ImageField(_("background image"),
                                         upload_to="hero/backgrounds/", blank=True, null=True)
    foreground_image = models.ImageField(_("foreground image"),
                                         upload_to="hero/foregrounds/", blank=True, null=True)
    text = models.CharField(_("text"), max_length=255, blank=True, null=True)
    position = models.PositiveIntegerField(
        _("position"), default=0, help_text=_("The order in which to display the hero."))
    start = models.DateTimeField(_("start"), db_index=True)
    end = models.DateTimeField(
        _("end"),
        db_index=True,
        help_text=_("The end time must be later than the start time."),
    )

    @property
    def is_active(self):
        right_now = datetime.datetime.now()

        if not self.start and not self.end:
            return True

        if self.start <= right_now and right_now <= self.end:
            return True

        if not self.start and right_now <= self.end:
            return True

        if not self.end and right_now >= self.start:
            return True

        return False

    def __str__(self):
        return self.name


class HeroCallToAction(models.Model):
    ANCHOR, BUTTON = 0, 1
    ACTION_TYPES = ((ANCHOR, "Anchor"), (BUTTON, "Button"))

    SELF, BLANK, PARENT, TOP = 0, 1, 2, 3
    TARGETS = ((SELF, "_self"), (BLANK, "_blank"),
               (PARENT, "_parent"), (TOP, "_top"),)

    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(_("position"), default=0, help_text=_(
        "The order in which to display the call to action."))
    action_type = models.PositiveIntegerField(
        _("action type"), choices=ACTION_TYPES, default=0)
    title = models.CharField(_("title"), max_length=50)
    link = models.CharField(_("link"), blank=True, null=True, max_length=255)
    target = models.PositiveBigIntegerField(
        _("target"), choices=TARGETS, default=0)

    def __str__(self):
        return self.title
