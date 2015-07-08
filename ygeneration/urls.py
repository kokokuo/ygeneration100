from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
	'',
	url(r'^$', 'ygeneration.views.home'),
	url(r'^home/$', 'ygeneration.views.home'),
	url(r'^activity_intro/$', 'ygeneration.views.activity_intro'),
	url(r'^team_intro/$', 'ygeneration.views.team_intro'),
	url(r'^facewall/index/$', 'facewall.views.index'),
	url(r'^fastquestion/index/$', 'fastquestion.views.index'),
	url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, documment_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)