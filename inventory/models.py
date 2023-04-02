from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0)

class MenuItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    item_price = models.FloatField(default=0.00)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time_ordered = models.DateTimeField(auto_now_add=True)
