from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pills, Medical, Plans, Schedule


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id','schedule']

class PillsSerializer(serializers.HyperlinkedModelSerializer):
    schedule = ScheduleSerializer(read_only = True, many=True)
    class Meta:
        model = Pills
        fields = ['id','pills','schedule' ,'exist', 'count']

class MedicalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medical
        fields = ['id','alergies']

class PlansSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plans
        fields = ['id','destination', 'date']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    pills = PillsSerializer(many=True)
    medical = MedicalSerializer( many=True)
    plans = PlansSerializer( many=True)
    class Meta:
        model = User
        fields = ['id','url','email','username','pills','medical','plans' ]
