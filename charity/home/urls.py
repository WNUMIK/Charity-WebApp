from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views, api

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.registration_view, name='register'),
    path('donation', views.AddDonation.as_view(), name='donation'),
    path('confirmation', views.DonationConfirmation.as_view(), name='confirmation'),
    path('profile', views.UserView.as_view(), name='profile'),
    path('get_institutions_by_category/', api.get_institutions_by_category, name='get_institutions_by_category'),
    path('crud', views.AdminView.as_view(), name='crud'),
]
