from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from users.forms import UserCreateForm
from django.utils.translation import ugettext_lazy as _


class RUserAdmin(UserAdmin):
    form = UserCreateForm
    fieldsets = (
        (None, {'fields': ('email', 'login',)}),
        (_('Permissions'),  {'fields': ('is_active', 'is_admin', 'is_superuser', 'latest_ip')}),
    )
    list_display = ('id', 'email', 'login', 'is_admin', 'latest_ip')
    list_filter = ('is_admin',)
    search_fields = ('email', 'login')
    ordering = ('-is_admin', 'id')

admin.site.register(User, RUserAdmin)
admin.site.unregister(Group)