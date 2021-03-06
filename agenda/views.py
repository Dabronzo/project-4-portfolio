from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Gig
from datetime import date
from .forms import GigCreateForm


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
            exclued_reject = queryset.exclude(status=3).order_by('event_date')
            # Pagination

            p = Paginator(exclued_reject, 8)
            page = request.GET.get('page')
            gigs_list = p.get_page(page)

            return render(
                request,
                'index.html',
                {
                    'gigs_list': gigs_list,
                }
            )


class GigDetail(View):
    """Class to render the detail page of
    a gig"""

    # def post(self, request, slug, *args, **kwargs):
    #     """Post method for acept or refuse a deal"""

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
                'venue': venue,
            }
        )


class AcceptGig(View):
    """View class to user acept a gig proposal"""

    def post(self, request, slug, *args, **kwargs):
        """Post method takeing the slug and changing the status of
        a gig on database"""

        gig = get_object_or_404(Gig, slug=slug)
        venue = gig.venue

        gig.status = 1
        gig.save()

        return render(
            request,
            'gig_detail.html',
            {
                'gig': gig,
                'venue': venue,
            }
        )


class RefuseGig(View):
    """View class to user refuse a gig proposal"""

    def post(self, request, slug, *args, **kwargs):
        """Post method takeing the slug and changing the status of
        a gig on database"""

        gig = get_object_or_404(Gig, slug=slug)

        gig.status = 3
        gig.save()

        return redirect('home')


class ManageGigs(View):
    """Class view for superuser manage all gigs"""
    today = date.today()

    def get(self, request, *args, **kwargs):
        """Get method to display all the gigs on a table"""

        queryset = Gig.objects.filter(event_date__gte=self.today).order_by('event_date')
        passed_gigs = Gig.objects.filter(event_date__lt=self.today).order_by('event_date')

        return render(
            request,
            'manage_gigs.html',
            {
                'all_gigs': queryset,
                'passed_gigs': passed_gigs
            }
        )

    # def post(self, request, slug, *args, **kwargs):
    #     """Post Method to make changes on the gig"""

    #     gig = get_object_or_404(Gig, slug=slug)




class DeleteGig(View):
    """Class method to delete a gig"""

    def post(self, request, slug, *args, **kwargs):
        """Post method to delete a gig"""

        gig = get_object_or_404(Gig, slug=slug)
        gig.delete()

        return redirect('manage_gigs')


class CreateGigForm(View):
    """Class to create Gigs"""

    def get(self, request, *args, **kwargs):
        """Get to the GigCreateForm"""

        form = GigCreateForm()
        return render(
            request,
            'create_gig.html',
            {
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        """Post the new Gig"""
        
        form = GigCreateForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('manage_gigs')


class UpdateGig(View):
    """Class to update gig"""

    def get(self, request, slug, *args, **kwargs):
        """Get method view form update"""

        gig = get_object_or_404(Gig, slug=slug)
        form = GigCreateForm(instance=gig)
        return render(
            request,
            'update_gigs.html',
            {
                'form': form,
                'gig': gig
            }
        )
    
    def post(self, request, slug, *args, **kwargs):
        """Post method to update"""

        gig = get_object_or_404(Gig, slug=slug)
        form = GigCreateForm(request.POST, instance=gig)
        if form.is_valid():
            form.save()

            return redirect('manage_gigs')

