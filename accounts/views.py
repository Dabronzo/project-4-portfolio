from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm




class LoginView (View):
    """Login class view"""

    def get(self, request):

        return render(
            request,
            'login.html'
        )
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass

class RegisterView(View):
    """Class to handle the Register View and authentication"""

    def get(self, request):
        form = RegistrationForm()
        return render(
            request,
            'register.html', {
                'form': form
            }
        )
    
    def post(self, request):
        """Post method for registration"""
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            return render(
                request,
                'register.html', {
                    'form': form
                }
            )

class UserLogOut(View):
    """View to log out"""

    def get(self, request):
        logout(request)
        return redirect('home')