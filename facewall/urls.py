# facewall/urls.py
from django.conf.urls import patterns, url

urlpatterns = patterns(
	'',
	url(r'^$', 'facewall.views.index', name="facewall_index"),
	url(r'^index/$', 'facewall.views.index', name="facewall_index"),
	url(r'^signup/$', 'facewall.views.add', name="facewall_add"),
)