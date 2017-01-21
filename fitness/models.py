from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)
    # The member that ate the food
    owner = models.ForeignKey('auth.User', related_name='foods')


class MemberInfo(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, related_name='user')
    age = models.IntegerField(default=18)
    feet = models.IntegerField(default=5)
    inches = models.IntegerField(default=11)
    weight = models.IntegerField(default=160)
