from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pills, Medical, Plans 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class PillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pills
        fields = ['']

class MedicalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medical
        fields = ['']

class PlansSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plans
        fields = ['']
