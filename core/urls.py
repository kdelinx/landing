from django.conf.urls import patterns, url

urlpatterns = patterns('core.views',
    url(r'^$', 'landing', name='landing'),
    url(r'^importcsv/$', 'importFromCSV', name='importcsv'),
)