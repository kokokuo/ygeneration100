# facewall/urls.py
from django.conf.urls import patterns, url

urlpatterns = patterns(
	'',
	url(r'^index/$', 'fastquestion.views.index', name="fastquestion_wall"),
	url(r'^video/$', 'fastquestion.views.get_face_video'),

	url(r'^index/(?P<page_id>\d)/$', 'fastquestion.views.get_page'),
)