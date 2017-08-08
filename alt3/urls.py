from django.conf.urls import patterns, include, url
from django.contrib import admin


from mainapp.views import index, examples, page, another_page, contact
from userManagementApp.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bluet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^examples/$', examples, name='examples'),
    url(r'^page/$', page, name='page'),
    url(r'^another_page/$', another_page, name='another_page'),
    url(r'^contact/$', contact, name='contact'),

)

urlpatterns += [
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
]
