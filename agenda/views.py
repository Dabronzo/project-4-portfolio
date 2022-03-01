from django.shortcuts import render
from django.views import generic, View
from .models import Gig



# class GigsList (generic.ListView):
#     """Class to display the list of gigs as index"""
#     model = Gig
#     queryset = Gig.objects.order_by('event_date')
#     template_name = 'index.html'
#     paginate_by = 8

#     def get(self, request, *args, **kwargs):
#         user_dj = self.request.user
#         if user_dj == None:
#             page = render(
#                 request, 'index.html'
#             )
#         else:
#             queryset = Gig.objects.filter(dj=user_dj).order_by('event_date')

#             page = render(
#                 request, 'index.html', {
#                    'object_list': queryset,
#                    'paginate_by': self.paginate_by 
#                 }
#             )
        
#         return page


class NewGigsList (View):

    def get(self, request, *args, **kwargs):
        paginate_by = 8
        dj_logged = self.request.user

        if dj_logged.id == None:
            return render(
                request, 'index.html'
            )  
        else:
            queryset = Gig.objects.filter(dj=dj_logged).order_by('event_date')

            return render(
            request,
            'index.html',
            {
                'object_list': queryset,
            }
        )


# Create your views here.
