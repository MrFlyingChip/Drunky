from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = models.ImageField()

    def __str__(self):
        return self.image.name

class Dish(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DrinkType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class CocktailType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date = models.DateField(verbose_name="Date", null=False, auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    alcohol = models.FloatField(default=0)
    likes = models.IntegerField(default=0)
    favourites = models.IntegerField(default=0)
    images = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    dishes = models.ManyToManyField(Dish, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.name


class Drink(Product):
    drinkType = models.ForeignKey(DrinkType, on_delete=models.CASCADE)


class Cocktail(Product):
    cocktailType = models.ForeignKey(CocktailType, on_delete=models.CASCADE)
    drinks = models.ManyToManyField(Drink)
    ingredients = models.ManyToManyField(Ingredient)
    tools = models.ManyToManyField(Tool)


class Bar(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    images = models.ManyToManyField(Image)
    favourites = models.IntegerField(default=0)
    comments = models.ManyToManyField(Comment, blank=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    weekday_text = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Account(User):
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, default=None, null=True)
    favouriteDrinks = models.ManyToManyField(Drink, default=None, blank=True)
    favouriteCocktails = models.ManyToManyField(Cocktail,default=None, blank=True)
    favouriteBars = models.ManyToManyField(Bar, default=None, blank=True)


class SortType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


