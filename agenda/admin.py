from django.contrib import admin
from .models import Venue, Gig

@admin.register(Gig)
class GigAdminManager(admin.ModelAdmin):

    list_display = ('event_name', 'event_date', 'dj', 'venue', 'status')
    prepopulated_fields = {'slug':('event_name',)}



admin.site.register(Venue)

# Register your models here.
