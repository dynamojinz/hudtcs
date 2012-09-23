from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hudtcs.views.home', name='home'),
    # url(r'^hudtcs/', include('hudtcs.foo.urls')),
    url(r'^$', 'tcs.teams.views.list'),
    url(r'^teams/(?P<team_id>\d+)/topics/list$', 'tcs.topics.views.list'),
    url(r'^topics/mytopics$', 'tcs.topics.views.mytopics'),
    url(r'^topics/(?P<topic_id>\d+)/show$', 'tcs.topics.views.show'),
    url(r'^topics/(?P<topic_id>\d+)/follow$', 'tcs.topics.views.follow'),
    url(r'^topics/new/team/(?P<team_id>\d+)$', 'tcs.topics.views.new'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'redirect_field_name':'/'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes':True}))

