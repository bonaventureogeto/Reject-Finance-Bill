from django.db import models

# Create your models here.


class ValueAddedTax(models.Model):
    fuel = models.CharField(max_length=255)
    cars = models.CharField(max_length=255)
    oxygen = models.CharField(max_length=255)

    def __str__(self):
        return self.fuel


class SocialHealth(models.Model):
    name = models.CharField(max_length=255)
    hospital = models.ForeignKey(ValueAddedTax, on_delete=models.CASCADE)
    payment_date = models.DateTimeField("date paid")

    def __str__(self):
        return self.name
