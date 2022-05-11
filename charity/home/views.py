from django.contrib.auth.models import Group
from django.db.models import Sum

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

from . import forms
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


def registration_view(request):
    form = forms.RegistrationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # regular_group = Group.objects.get(name='regular')
            # user.groups.add(regular_group)
        return redirect(reverse('home:login'))
    return render(request, 'home/register.html', {'form': form})




class AddDonation(TemplateView):
    template_name = 'home/donation.html'
