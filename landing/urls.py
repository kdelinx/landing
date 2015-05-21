from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout, password_reset
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^error404/$', 'core.views.page_404', name='core_404'),
    url(r'^$', 'core.views.index', name='index'),
    url(r'^landing/', include('core.urls', namespace='landing')),
    url(r'^profile/', include('users.urls', namespace='users')),
    url(r'login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^register/$', 'users.views.register', {'autologin': settings.LOGIN_AFTER_SIGNUP}, name='register'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^about/$', 'core.views.about', name='about'),
    url(r'^tos/$', 'core.views.tos', name='tos'),
    url(r'password_reset/$', password_reset, name='password_reset'),
    url(r'resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'core.views.page_404'