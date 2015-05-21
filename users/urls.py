from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',
    url(r'^$', 'profile', name='profile'),
    url(r'^(?P<id>\d+)/$', 'otherProfile', name='otherProfile'),
)