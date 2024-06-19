from django.http import HttpResponse
from django.shortcuts import render
from .models import ValueAddedTax
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. PAY YOUR TAXES.")


def valueAddedTax(request):
    tax_list = ValueAddedTax.objects.all()
    context = {
        "tax_list": tax_list,
    }
    return render(request, "index.html", context)


def socialHealth(request):
    return HttpResponse("You're BROKE!")
