from . import views
from django.urls import path

urlpatterns = [
    path('', views.NewGigsList.as_view(), name='home'),
    path('details/<slug:slug>', views.GigDetail.as_view(), name='gig_detail'),
    path('accept/<slug:slug>', views.AcceptGig.as_view(), name='gig_accept'),
    path('refuse/<slug:slug>', views.RefuseGig.as_view(), name='gig_refuse'),
    path('manager', views.ManageGigs.as_view(), name='manage_gigs'),

]
