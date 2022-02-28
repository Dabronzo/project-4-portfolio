from . import views
from django.urls import path

urlpatterns = [
    path('', views.GigsList.as_view(), name='home'),
]
