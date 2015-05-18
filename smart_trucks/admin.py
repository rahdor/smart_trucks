from django.contrib import admin
from smart_trucks.models import Event, Truck

# Register your models here.


# for displaying trucks
class TruckAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['name']}),
	]


# for displaying trucks that will be at an event
class TruckInline(admin.TabularInline):
	model = Event.trucks.through
	

# for displaying events
class EventAdmin(admin.ModelAdmin):
	list_filter = ['start_time']

	fieldsets = [
	(None, {'fields': ['location']}),
	('Date', {'fields': ['start_time']}),
	]
	inlines = [TruckInline]
	


admin.site.register(Event, EventAdmin)
admin.site.register(Truck, TruckAdmin)
