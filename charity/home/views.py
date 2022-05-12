from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.db.models import Sum

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

from . import forms
from .models import Donation, Institution, Category


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


def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('home:home'))
        else:
            return redirect(reverse('home:register'))
    else:
        form = forms.LoginForm()

    return render(request, 'home/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(reverse('home:home'))


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

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['category'] = Category.objects.all()
        ctx['institution'] = Institution.objects.all()

        return ctx

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        donation = Donation()
        form = forms.DonationForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                donation = form.save(commit=False)
                donation.save()
            return redirect(reverse('home:donation-confirmation'))
        return render(reverse('home:donation'))

