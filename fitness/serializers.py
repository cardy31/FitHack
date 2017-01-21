from rest_framework import serializers
from django.contrib.auth.models import User
from fitness.models import MemberInfo, Food


class FoodSerializer(serializers.ModelSerializer):
    # The owner of a food entry is the member who ate it
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Food
        fields = ('id', 'name', 'calories', 'datetime', 'owner')


class MemberInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MemberInfo
        fields = ('id', 'age', 'feet', 'inches', 'weight', 'owner')


# Implements a special user class that has built-in login/out abilities
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Will be a list of all the foods a member has eaten
    foods = serializers.HyperlinkedRelatedField(many=True, view_name='food-detail', read_only=True)
    memberinfo = serializers.HyperlinkedRelatedField(many=True, view_name='memberinfo-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'foods', 'memberinfo')
