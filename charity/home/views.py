from django.db.models import Sum

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Donation, Institution


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['quantity'] = Donation.objects.all().aggregate(Sum('quantity'))['quantity__sum']
        ctx['institution'] = Donation.objects.all().count()
        ctx['fundations'] = Institution.objects.all().filter(type=0)
        ctx['organizations'] = Institution.objects.all().filter(type=1)
        ctx['local'] = Institution.objects.all().filter(type=2)

        return ctx


class LoginView(TemplateView):
    template_name = 'home/login.html'


class RegisterView(TemplateView):
    template_name = 'home/register.html'



class AddDonation(TemplateView):
    template_name = 'home/donation.html'
