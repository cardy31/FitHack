from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)
    # The member that ate the food
    owner = models.ForeignKey('auth.User', related_name='foods')

#Comment to commit...
class MemberInfo(models.Model):
    age = models.IntegerField(default=18)
    feet = models.IntegerField(default=5)
    inches = models.IntegerField(default=11)
    weight = models.IntegerField(default=160)
    owner = models.ForeignKey('auth.User', related_name='memberinfo', default=1)
