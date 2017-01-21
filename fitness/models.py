from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)
    # The member that ate the food
    owner = models.ForeignKey('auth.User', related_name='foods')


class MemberInfo(models.Model):
    age = models.IntegerField(default=18)
    feet = models.IntegerField(default=5)
    inches = models.IntegerField(default=11)
    weight = models.IntegerField(default=160)
