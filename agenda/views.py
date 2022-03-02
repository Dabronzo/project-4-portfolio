from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Gig

# Paginator
from django.core.paginator import Paginator


class NewGigsList (View):
    """View class to display the gigs according to the user logged in
    and display the gigs with pagination"""


    def get(self, request, *args, **kwargs):
        """Method to get a list of gigs if
        the user is not anonymous"""

        dj_logged = self.request.user

        if dj_logged.id is None:
            return render(
                request, 'index.html'
            )  
        else:
            queryset = Gig.objects.filter(dj=dj_logged).order_by('event_date')
            # Pagination

            p = Paginator(queryset, 8)
            page = request.GET.get('page')
            gigs_list = p.get_page(page)

            return render(
            request,
            'index.html',
            {
                'object_list': queryset,
                'gigs_list': gigs_list,
            }
        )


class GigDetail(View):
    """Class to render the detail page of
    a gig"""

    def get(self, request, slug, *args, **kwargs):
        """Get method to render the gig details"""
        queryset = Gig.objects.all()
        gig = get_object_or_404(queryset, slug=slug)
        venue = gig.venue

        return render(
            request,
            'gig_detail.html',
            {
                'gig': gig,
                'venue': venue
            }
        )
