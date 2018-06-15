from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = models.ImageField()


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
    images = models.ManyToManyField(Image)
    dishes = models.ManyToManyField(Dish)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.name


class Drink(Product):
    drinkType = models.ForeignKey(DrinkType, on_delete=models.CASCADE)


class Cocktail(Product):
    cocktailType = models.ForeignKey(CocktailType, on_delete=models.CASCADE)
    drinks = models.ManyToManyField(Drink)
    ingredients = models.ManyToManyField(Ingredient)
    tools = models.ManyToManyField(Tool)


class Account(User):
    photo = models.ForeignKey(Image, on_delete=models.CASCADE)




