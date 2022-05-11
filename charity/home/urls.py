from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.registration_view, name='register'),
    path('donation', views.AddDonation.as_view(), name='donation'),
]
