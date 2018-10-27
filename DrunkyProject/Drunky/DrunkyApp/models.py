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


class MeasureType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DrinkType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class CocktailType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateField(verbose_name="Date", null=False, auto_now=True)

    def __str__(self):
        return self.text


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

    def getComments(self):
        comments = self.comments.all()
        comment_to_account = CommentToAccount.objects.filter(comment__in=comments)
        return comment_to_account

class Drink(Product):
    drinkType = models.ForeignKey(DrinkType, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    @staticmethod
    def addCommentToDrink(drink_id, comment):
        drink = Drink.objects.get(pk=drink_id)
        drink.comments.add(comment)

class DrinkTypeMeasure(models.Model):
    drinksType = models.ForeignKey(DrinkType, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    measureType = models.ForeignKey(MeasureType, on_delete=models.CASCADE)


class DrinkMeasure(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    measureType = models.ForeignKey(MeasureType, on_delete=models.CASCADE)


class IngredientMeasure(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    measureType = models.ForeignKey(MeasureType, on_delete=models.CASCADE)


class Cocktail(Product):
    cocktailType = models.ForeignKey(CocktailType, on_delete=models.CASCADE)
    drinksType = models.ManyToManyField(DrinkTypeMeasure, blank=True)
    drinks = models.ManyToManyField(DrinkMeasure, blank=True)
    ingredients = models.ManyToManyField(IngredientMeasure, blank=True)
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
    likedDrinks = models.ManyToManyField(Drink, default=None, blank=True, related_name='liked_drinks')
    likedCocktails = models.ManyToManyField(Cocktail,default=None, blank=True, related_name='liked_cocktails')
    likedBars = models.ManyToManyField(Bar, default=None, blank=True, related_name='liked_bars')
    favouriteDrinks = models.ManyToManyField(Drink, default=None, blank=True, related_name='favourite_drinks')
    favouriteCocktails = models.ManyToManyField(Cocktail,default=None, blank=True, related_name='favourite_cocktails')
    favouriteBars = models.ManyToManyField(Bar, default=None, blank=True, related_name='favourite_bars')

    def addProductToArray(self, model, model_id, array):
        product = model.objects.get(pk=model_id)
        if(product not in array.all()):
            array.add(product)

    def removeProductFromArray(self, model, model_id, array):
        product = model.objects.get(pk=model_id)
        if(product in array.all()):
            array.remove(product)

    def likeProduct(self, model, model_id, array):
        product = model.objects.get(pk=model_id)
        if(product not in array.all()):
            product.likes += 1
            product.save(update_fields=['likes'])
            array.add(product)

    def unlikeProduct(self, model, model_id, array):
        product = model.objects.get(pk=model_id)
        if(product in array.all()):
            product.likes -= 1
            product.save(update_fields=['likes'])
            array.remove(product)
    
class CommentToAccount(models.Model):
    account = models.ForeignKey(Account, null=False, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.username + ": " + self.comment.text
    
    @staticmethod
    def createComment(comment_text, username):
        new_comment = Comment(text=comment_text)
        new_comment.save()
        acc = Account.objects.get(username=username)
        new_comment_to_acc = CommentToAccount(comment=new_comment, account=acc)
        new_comment_to_acc.save()
        return new_comment


class SortType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


