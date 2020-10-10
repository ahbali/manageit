import datetime
from django.utils import timezone
from manager.models import Equipment, Person, SSLCert, Software, SupportContract
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
# home:
#         nombre d'équipement,
#         nombre des application,
#         nombre de Personel,
#         warning(date de fin de vie/support proche 6 mois),
#         Problème(fin de vie/support),
#         Recherche application/serveur: (nom, IP, date de mise en prod, date de fin de vie,
#         date de fin de support),


def index(request):
    number_of_equipment = Equipment.objects.count()
    number_of_apps = Software.objects.count()
    number_of_persons = Person.objects.count()
    warnings_equipment = Equipment.objects.filter(
        license_end__gt=timezone.now(),
        license_end__lte=timezone.now() + datetime.timedelta(days=6 * 30),
    )
    problems_equipment = Equipment.objects.filter(license_end__lt=timezone.now())
    warnings_equipment_support = Equipment.objects.filter(
        support__expiration_date__gt=timezone.now(),
        support__expiration_date__lte=timezone.now() + datetime.timedelta(days=6 * 30),
    )
    problems_equipment_support = Equipment.objects.filter(
        support__expiration_date__lt=timezone.now()
    )
    warnings_ssl_cert = SSLCert.objects.filter(
        expiration_date__gt=timezone.now(),
        expiration_date__lte=timezone.now() + datetime.timedelta(days=6 * 30),
    )
    problem_ssl_cert = SSLCert.objects.filter(expiration_date__lt=timezone.now())
    problems_count = (
        problems_equipment.count()
        + problems_equipment_support.count()
        + problem_ssl_cert.count()
    )
    warnings_count = (
        warnings_equipment.count()
        + warnings_equipment_support.count()
        + warnings_ssl_cert.count()
    )
    context = {
        "number_of_equipment": number_of_equipment,
        "number_of_apps": number_of_apps,
        "number_of_persons": number_of_persons,
        "warnings_equipment": warnings_equipment,
        "warnings_equipment_support": warnings_equipment_support,
        "warnings_ssl_cert": warnings_ssl_cert,
        "problems_equipment": problems_equipment,
        "problems_equipment_support": problems_equipment_support,
        "problems_ssl_cert": problem_ssl_cert,
        "problems_count": problems_count,
        "warnings_count": warnings_count,
    }
    return render(request, "manager/index.html", context)


class EquipmentListView(ListView):
    model = Equipment


class SoftwareListView(ListView):
    model = Software


class PersonListView(ListView):
    model = Person


class SSLCertListView(ListView):
    model = SSLCert


class SupportContractListView(ListView):
    model = SupportContract


class EquipmentDetailView(DetailView):
    model = Equipment


class SoftwareDetailView(DetailView):
    model = Software


class PersonDetailView(DetailView):
    model = Person


class SSLCertDetailView(DetailView):
    model = SSLCert


class SupportContractDetailView(DetailView):
    model = SupportContract
