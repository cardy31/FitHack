from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True)  # validators should be a list
    age = models.IntegerField
    height = models.IntegerField
    weight = models.IntegerField

class Food(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField()
    datetime = models.DateTimeField()