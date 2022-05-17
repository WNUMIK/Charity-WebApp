from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.db.models import Sum

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from .forms import RegistrationForm, LoginForm
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


# class Login(View):
#     def get(self, request):
#         form = LoginForm(request, request.POST)
#         return render(request, 'home/login.html', {'form': form})
#
#     def post(self, request):
#         form = LoginForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#
#             user = authenticate(email=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect(reverse('home:home'))
#         else:
#             return redirect(reverse('home:register'))


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


@login_required
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


class AddDonation(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        context = {
            'categories': categories,
            'institutions': institutions,
        }
        return render(request, 'home/donation.html', context)


class DonationConfirmation(LoginRequiredMixin, View):
    def post(self, request):
        quantity = request.POST.get("bags")
        categories = request.POST.getlist("categories")
        institution = request.POST.get("organization")
        address = request.POST.get("address")
        city = request.POST.get("city")
        postcode = request.POST.get("postcode")
        phone = request.POST.get("phone")
        data = request.POST.get("data")
        time = request.POST.get("time")
        more_info = request.POST.get("more_info")

        donation = Donation.objects.create(
            quantity=quantity,
            institution=Institution.objects.get(id=institution),
            address=address,
            phone_number=phone,
            city=city,
            zip_code=postcode,
            pick_up_date=data,
            pick_up_time=time,
            pick_up_comment=more_info,
            user=request.user,
        )
        donation.categories.set(categories)
        return render(request, 'home/form-confirmation.html')

# @login_required
# def donation_view(request):
#     form = DonationForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#         return redirect(reverse_lazy('home:confirmation'))
#     ctx = {'category': Category.objects.all(), 'institution': Institution.objects.all(), "form": form}
#     return render(request, "home/donation.html", ctx)


# @login_required
# def confirmation_view(request):
#     return render(request, 'home/form-confirmation.html')

class UserView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        donations = Donation.objects.filter(user=request.user).order_by('pick_up_date', 'pick_up_time')
        return render(request, 'home/user.html', {'user': user, 'donations': donations})


# def get_institutions_by_category(request):
#     categories_ids = request.GET.getlist('categories_ids')
#     if categories_ids is not None:
#         institutions = Institution.objects.filter(categories__in=categories_ids).distinct()
#     else:
#         institutions = Institution.objects.all()
#     return render(request, "home/api_institutions.html", {'institutions': institutions})