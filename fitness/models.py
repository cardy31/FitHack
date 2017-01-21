from django.db import models


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField
    phone_number = models.
    age
    height
    weight