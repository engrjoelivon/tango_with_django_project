from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
                       #url(r'^$', "rango.views.home"),
                       url(r'^rango$', include(urls))

)
