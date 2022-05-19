from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = 'Charity Donation Admin Panel'


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')
    list_filter = ('name', 'surname', 'email')
    search_fields = ('surname', 'email')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(models.Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_categories', 'type')
    list_filter = ('name', 'type',)
    search_fields = ('name', 'type',)


@admin.register(models.Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'quantity', 'institution',)
    list_filter = ('user',)
    search_fields = ('user',)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'message')
    list_filter = ('name', 'surname', 'email')
    search_fields = ('surname', 'email')
