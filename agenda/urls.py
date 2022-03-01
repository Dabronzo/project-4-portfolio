from . import views
from django.urls import path

urlpatterns = [
    path('', views.NewGigsList.as_view(), name='home'),
]
