from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^customers/$', 'customers.views.index'),
    url(r'^customers/(?P<customer_id>\d+)/$', 'customers.views.detail'),
    url(r'^customers/(?P<customer_id>\d+)/results/$', 'customers.views.results'),
    url(r'^customers/(?P<customer_id>\d+)/work/$', 'customers.views.work'),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
