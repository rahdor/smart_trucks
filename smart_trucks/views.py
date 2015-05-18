from django.shortcuts import render
from django.http import HttpResponse
from models import Event, Truck
from datetime import datetime, timedelta, time, date

from dateutil import parser as dateparser
from dateutil import tz

import requests

from django.template import RequestContext, loader
import pytz

# Create your views here.

# reload page:
def reload(request):
	events = Event.objects.all()
	today = datetime.now().date()
	tomorrow = today + timedelta(1)
	today_start = datetime.combine(today, time())
	today_end = datetime.combine(tomorrow, time())
	ACCESS_TOKEN = "763243537095040|00a432f1c89c59a884e9103dd92eafcf"
	OFF_THE_GRID_URL = "https://graph.facebook.com/OffTheGridSF/events?access_token="
	CHECKDATE = date.today()-timedelta(days = 30)
	events_json = requests.get(OFF_THE_GRID_URL + ACCESS_TOKEN).json()
	
	# add all trucks to database
	FILENAME = 'vendors.txt'
	for line in open(FILENAME, 'r'):
		name = line.rstrip()
		if len(Truck.objects.filter(name = name)) == 0:
			q = Truck(name = line.rstrip())
			q.save()

	trucks = Truck.objects.all()

	# function to add one page of events to database - adds events that haven't happened yet
	def add_to_database(events):
		for event in events:			
			# start time is in pst!
			start_time = dateparser.parse(event['start_time']) 
			date = start_time.date()
			print start_time.date()
			print CHECKDATE
			if start_time.date() < CHECKDATE:
				return False
			facebook_id = event['id']

			if len(Event.objects.filter(facebook_id = facebook_id)) == 0:
					
				if 'end_time' not in event.keys():
					end_time = datetime.now()
				else:
					end_time = dateparser.parse(event['end_time'])
				if 'location' not in event.keys():
					location = None
				else:
					location = event['location']
				name = event['name']

				q = Event(end_time = end_time, location = location, name = name, start_time = start_time, facebook_id = facebook_id, date = date)
				
				q.save()

				# set relationship with trucks 
				event_url = 'https://graph.facebook.com/' + facebook_id + '?access_token=' + ACCESS_TOKEN
				event_json = requests.get(event_url).json()

				for truck in trucks:
					if truck.name in event_json['description']:
						q.trucks.add(truck)

		return True


	# adds first page to database, then parses through the rest of the events
	check = add_to_database(events_json['data'])
	while('next' in events_json['paging'].keys() and check):
		events_json = requests.get(events_json['paging']['next']).json()
		check = add_to_database(events_json['data'])
		
	# delete events from db that are more than 30 days old
	Event.objects.filter(start_time__lte = datetime.today()-timedelta(days=30)).delete()
	# display
	template = loader.get_template('smart_trucks/reload.html')
	return render(request, 'smart_trucks/reload.html', {})





def home_page(request):
	events = Event.objects.all()

	#we want to get the (datetime of today - timedelta(hours = 8)).date()
	today = (datetime.now() - timedelta(hours = 8)).date()

	tomorrow = today + timedelta(days = 1)	

	# adding 8 hours because of utc conversion
	today_start = datetime(today.year, today.month, today.day) 
	tomorrow_start = datetime(tomorrow.year, tomorrow.month, tomorrow.day) 

	
	pst = pytz.timezone('US/Pacific')
	# daily_events_2 = Event.objects.filter(date = datetime.now(tz=pst).date())
	# print today_start
	# print 'hello'
	# print tomorrow_start
	print datetime.today()
	daily_events = Event.objects.filter(start_time__gte = today_start, start_time__lte = tomorrow_start)

	# daily_events = Event.objects.filter(start_time__gte = today_start, start_time__lte = tomorrow_start)	
	for event in daily_events:
		print event.date
	template = loader.get_template('smart_trucks/index.html')
	
	context = {'latest_event_list': daily_events}
	return render(request, 'smart_trucks/index.html', context)
	# each event has its own app id - follow app id to get event page

	# parse description for trucks 
	# do frequency/etc. 



def event_page(request, event_id):
	event = Event.objects.get(pk = event_id)
	response = "You're looking at Off the Grid at the %s on %s"
	d = str(event.start_time)
	l = str(event.location)

	truck_list = event.trucks.all()
	template = loader.get_template('smart_trucks/event.html')
	
	context = {'event_name': event.name, 'truck_list': truck_list}
	return render(request, 'smart_trucks/event.html', context)
	# return HttpResponse(response % (l, d))



def truck_page(request, truck_id):
	def get_frequency():
		count = 0
		truck = Truck.objects.get(id = truck_id)
		eventlist = []
		pst = pytz.timezone('US/Pacific')
		today = datetime.now(tz=pst).date()
		thirtydays = (datetime.now(tz = pst) - timedelta(days = 30)).date()
		for event in Event.objects.filter(date__lte = today, date__gte = thirtydays):
			if truck in event.trucks.all():
				eventlist.append(event)
				count += 1
		return count, eventlist
	frequency, eventlist = get_frequency()
	truck = Truck.objects.get(pk = truck_id)
	template = loader.get_template('smart_trucks/truck.html')

	context = {'event_list':eventlist, 'truck_name':truck.name, 'frequency':frequency}
	return render(request, 'smart_trucks/truck.html', context)

	# return HttpResponse(response)
	

