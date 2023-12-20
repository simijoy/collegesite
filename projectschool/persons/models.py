from django.db import models

# Create your models here.
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    department = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    # name = models.CharField(max_length=124)
    department = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


