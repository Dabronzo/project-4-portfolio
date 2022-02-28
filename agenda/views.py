from django.shortcuts import render
from django.views import generic
from .models import Gig



class GigsList (generic.ListView):
    """Class to display the list of gigs as index"""
    model = Gig
    queryset = Gig.objects.order_by('event_date')
    template_name = 'index.html'
    paginate_by = 8


# Create your views here.
