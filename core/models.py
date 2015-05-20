#coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Landing():
    domen = models.CharField(
        _('Domain'),
        max_length=255,
    )
    server_path = models.CharField(
        _('Server path'),
        max_length=255,
    )
    link = models.URLField(
        _('Link path'),
        blank=False,
        null=False,
        max_length=255,
    )
    phoneIsPic = models.BooleanField(
        _('Phone as picture'),
        default=False,
    )
    phoneIsText = models.BooleanField(
        _('Phone as text'),
        default=False,
    )
    linkPhonePic = models.URLField(
        _('Phone link'),
        null=True,
        blank=True,
        max_length=255,
    )
    emailIsPic = models.BooleanField(
        _('Email is picture'),
        default=False,
    )
    emailIsText = models.BooleanField(
        _('Email is text'),
        default=False,
    )
    linkEmailPic = models.URLField(
        _('Email picture link'),
        null=True,
        blank=True,
        max_length=255,
    )
    visit = models.BooleanField(
        _('Visit state'),
        default=False,
    )
    visitLink = models.CharField(
        _('Domain for visit'),
        max_length=150,
    )
    visitDomain = models.URLField(
        
    )