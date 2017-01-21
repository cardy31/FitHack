from rest_framework import serializers
from django.contrib.auth.models import User
from fitness.models import Member, Food


class MemberSerializer(serializers.ModelSerializer):
    # Will be a list of all the foods a member has eaten
    foods = serializers.HyperlinkedRelatedField(many=True, view_name='food-detail', read_only=True)

    class Meta:
        model = Member
        fields = ('id', 'email', 'phone_number', 'age', 'height', 'weight', 'foods')


class FoodSerializer(serializers.ModelSerializer):
    # The owner of a food entry is the member who ate it
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Food
        fields = ('id', 'name', 'calories', 'datetime', 'owner')