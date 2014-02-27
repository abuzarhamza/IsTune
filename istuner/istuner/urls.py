from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'istuner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rango/$',include('rango.urls')), #my test appliaction
    url(r'^rango/about/$',include('rango.urls')), #my test appliaction
    url(r'^admin/', include(admin.site.urls)),
)
