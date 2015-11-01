"""
Definition of urls for djangocon.
"""

from datetime import datetime
from django.conf.urls import patterns, url

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'app.views.home', name='home'),
    url(r'^append/$','app.views.append',name='append'),
    url(r'^broadcast/$','app.views.broadcast',name='broadcast'),
    url(r'^cancel/$','app.views.cancel',name='cancel'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
