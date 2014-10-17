from django.conf.urls import patterns, include, url

from django.contrib import admin
from views import home
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', home.as_view(), name='home'),
)
