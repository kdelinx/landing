from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from users.forms import UserCreateForm



class RUserAdmin(UserAdmin):
    form = UserCreateForm
    ## TODO Add admin forms

# admin.site.register()
admin.site.unregister(Group)