from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vat/", views.valueAddedTax, name="vat"),
    path("social/", views.socialHealth, name="social"),

]
