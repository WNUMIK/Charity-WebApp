from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.db.models import Sum

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from .forms import DonationForm, RegistrationForm, LoginForm
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
        form = LoginForm(request, request.POST)

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
        form = LoginForm()

    return render(request, 'home/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(reverse('home:home'))


def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # regular_group = Group.objects.get(name='regular')
            # user.groups.add(regular_group)
        return redirect(reverse('home:login'))
    return render(request, 'home/register.html', {'form': form})


def donation_view(request):
    if request.method == 'POST':
        donation = Donation()
        form = DonationForm(request, request.POST)
        if form.is_valid():
            donation.quantity = form.cleaned_data['bags']
            donation.address = form.cleaned_data['address']
            donation.phone_number = form.cleaned_data['phone']
            donation.city = form.cleaned_data['city']
            donation.zip_code = form.cleaned_data['postcode']
            donation.pick_up_date = form.cleaned_data['data']
            donation.pick_up_time = form.cleaned_data['time']
            donation.pick_up_comment = form.cleaned_data['more_info']
            donation.save()
        return redirect(reverse_lazy('home:donation-confirmation'))
    else:
        form = DonationForm()
    ctx = {'category': Category.objects.all(), 'institution': Institution.objects.all(), "form": form}
    return render(request, "home/donation.html", ctx)


class ConfirmDonation(TemplateView):
    template_name = 'home/form-confirmation.html'
