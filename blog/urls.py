from django.conf.urls import patterns, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^(?P<page>\d+)?/?$', views.BlogIndex.as_view(), name="index"),
	url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)
