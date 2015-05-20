#coding: utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('Email'),
        max_length=150,
        unique=True,
    )
    login = models.CharField(
        _('Login'),
        max_length=150,
        unique=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_admin = models.BooleanField(
        default=True,
    )
    last_activity = models.DateField(
        default=timezone.now()
    )
    latest_ip = models.IPAddressField(
        default=0,
    )

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _(u'Пользователь')
        verbose_name_plural = _(u'Пользователи')


    def __unicode__(self):
        return self.login


    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        return self.is_admin
