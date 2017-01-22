from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=50, default="Cheese")
    brandName = models.CharField(max_length=50, default="N/A")
    servingQuantity = models.IntegerField(default=1)
    servingUnit = models.CharField(default="Kiwi", max_length=50)
    calories = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    totalFats = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    satFats = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    cholesterol = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    sodium = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    carbs = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    sugar = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    protein = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    thumb = models.URLField(default="localhost")
    highres = models.URLField(default="localhost")
    datetime = models.DateTimeField(auto_now=True)
    # The member that ate the food
    owner = models.ForeignKey('auth.User', related_name='foods')


class HistoricWeight(models.Model):
    weight = models.IntegerField(default=160)
    datetime = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='historicweightinfo', default=1)


class MemberInfo(models.Model):
    age = models.IntegerField(default=18)
    feet = models.IntegerField(default=5)
    inches = models.IntegerField(default=11)
    weight = models.IntegerField(default=160)
    goalWeight = models.IntegerField(default=160)
    plan = models.IntegerField(default=0)
    # The member whose information this is
    owner = models.ForeignKey('auth.User', related_name='memberinfo', default=1)



