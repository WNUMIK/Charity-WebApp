from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'


class LoginView(TemplateView):
    template_name = 'home/login.html'


class RegisterView(TemplateView):
    template_name = 'home/register.html'


class AddDonation(TemplateView):
    template_name = 'home/donation.html'
