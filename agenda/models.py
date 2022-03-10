from django.db import models
from accounts.models import NewUserDj
from datetime import date

STATUS = ((0, 'Proposal'), (1, 'Approved'), (3, 'Rejected'))


class Venue (models.Model): 
    """Class to set the Venues"""
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=100, default='city name')
    venue_link = models.CharField(max_length=100, unique=True)
    additional_info = models.TextField(blank=True)
    contact_info = models.CharField(max_length=50)
    emergency_info = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"   


class Gig (models.Model):
    """Class to set the gigs"""
    event_name = models.CharField(max_length=50, unique=True, default='party-')
    event_date = models.DateTimeField()
    play_time = models.CharField(max_length=50, default='E.g.: 2 hours')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    dj = models.ForeignKey(
        NewUserDj, on_delete=models.CASCADE, related_name='gig_event')
    status = models.IntegerField(choices=STATUS, default=0)
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='gig_venue'
    )
    fees = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    info_notes = models.TextField(blank=True)

    def days_to(self):
        """Function to get the difference
        between days"""
        today = date.today()
        days_till = self.event_date.date() - today
        return days_till

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Gig on {self.event_date} at the {self.venue.name} featuring {self.dj.user_name}"
