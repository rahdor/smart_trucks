from django.conf.urls import patterns, url

from smart_trucks import views

urlpatterns = patterns('', 
	#home page (complete listing)
	url(r'^$', views.home_page, name = 'home_page'),
	
	# url for event pages not sure about syntax....
	url(r'^events/(?P<event_id>\d+)/$', views.event_page, name = 'event_page'),

	# url to load all the objects into the database
	url(r'^reload/$', views.reload, name = 'reload'),

	#url for truck pages
	url(r'^trucks/(?P<truck_id>\d+)/$', views.truck_page, name = 'truck')


)


