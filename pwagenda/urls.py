from django.conf.urls import patterns, url
from pwagenda import views

urlpatterns = patterns('',
	url(r'^$', views.homepage, name='homepage'),
	url(r'^index/$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^meet-the-team/$', views.meet_the_team, name='team'),
	url(r'^meeting/(?P<meeting_name_slug>[\w\-]+)/$', views.meeting, name='meeting'),
	url(r'^add_meeting/$', views.add_meeting, name='add_meeting'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),

)