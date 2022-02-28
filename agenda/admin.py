from django.contrib import admin
from .models import Venue, Gig

@admin.register(Gig)
class GigAdminManager(admin.ModelAdmin):

    prepopulated_fields = {'slug':('event_name',)}



admin.site.register(Venue)

# Register your models here.
