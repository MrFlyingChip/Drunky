from django.db import models


# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)


class Image(models.Model):
    image = models.ImageField()


class DrinkType(models.Model):
    name = models.CharField(max_length=50)


class Country(models.Model):
    name = models.CharField(max_length=50)


class CocktailType(models.Model):
    name = models.CharField(max_length=50)