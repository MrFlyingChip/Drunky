from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = models.ImageField()


class Dish(models.Model):
    name = models.CharField(max_length=50)


class DrinkType(models.Model):
    name = models.CharField(max_length=50)


class Country(models.Model):
    name = models.CharField(max_length=50)


class CocktailType(models.Model):
    name = models.CharField(max_length=50)


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date = models.DateField(verbose_name="Date", null=False, auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    alcohol = models.FloatField(default=0)
    votes = models.IntegerField(default=0)
    averageMark = models.FloatField(default=0)
    images = models.ManyToManyField(Image)
    dishes = models.ManyToManyField(Dish)
    comments = models.ManyToManyField(Comment)


class Drink(Product):
    drinkType = models.ForeignKey(DrinkType, on_delete=models.CASCADE)




