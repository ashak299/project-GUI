"""
Definition of urls for project.
"""

from django.conf.urls import include, url
from App import views
from App.views import EncryptPage
import App.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', project.views.home, name='home'),
    # url(r'^project/', include('project.project.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', App.views.index, name='index'),
    url(r'^home$', App.views.index, name='home'),
    url(r'^EncryptPage$', App.views.EncryptPage, name='EncryptPage'),
    url(r'^DecryptPage$', App.views.DecryptPage, name='DecryptPage')
]
