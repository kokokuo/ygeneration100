from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
	'',
	url(r'^$', 'ygeneration.views.home', name='home'),
	url(r'^home/$', 'ygeneration.views.home', name='home'),
	url(r'^activity_intro/$', 'ygeneration.views.activity_intro', name='activity_intro'),
	url(r'^team_intro/$', 'ygeneration.views.team_intro', name="team_intro"),
	url(r'^facewall/index/$', 'facewall.views.index'),
	url(r'^facewall/signup/$', 'facewall.views.add', name="facewall_add"),
	url(r'^fastquestion/index/$', 'fastquestion.views.index'),
	url(r'^bepci/admin/', include(admin.site.urls)),
)

# Custion 404 views and page
handler404 = 'ygeneration.views.error404'
# Custion 500 views and page
handler500 = 'ygeneration.views.error500'

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, documment_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)