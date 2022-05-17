from django.shortcuts import render

from .models import Institution


def get_institutions_by_category(request):
    categories_ids = request.GET.getlist('categories_ids')
    if categories_ids is not None:
        institutions = Institution.objects.filter(categories__in=categories_ids).distinct()
    else:
        institutions = Institution.objects.all()
    return render(request, "home/api_institutions.html", {'institutions': institutions})