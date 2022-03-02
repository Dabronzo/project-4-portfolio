from . import views
from django.urls import path

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.UserLogOut.as_view(), name='logout')
]