from django.conf.urls import patterns, url

urlpatterns = patterns('core.views',
    url(r'^$', 'landing', name='landing'),
    url(r'^importcsv/$', 'importFromCSV', name='importcsv'),
    url(r'^info/(?P<id>\d+)$', 'landing_id', name='landing_id'),
    url(r'^delete/(?P<id>\d+)$', 'landing_delete', name='landing_delete'),
    url(r'^create/$', 'landing_create', name='landing_create'),
    url(r'^fullpage/$', 'landing_full', name='landing_full'),
)