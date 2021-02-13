from django.contrib.auth.models import User
from pills.models import Medical, Schedule, Pills, Plans
from rest_framework import viewsets
from rest_framework import permissions
from pills.serializers import UserSerializer, PillsSerializer, MedicalSerializer, PlansSerializer, ScheduleSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

# class PillsViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Pills.objects.all()
#     serializer_class = PillsSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class ScheduleViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Schedule.objects.all()
#     serializer_class = ScheduleSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class PlansViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Plans.objects.all()
#     serializer_class = PlansSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class MedicalViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Medical.objects.all()
#     serializer_class = MedicalSerializer
#     permission_classes = [permissions.IsAuthenticated]

# https://www.django-rest-framework.org/api-guide/views/#function-based-views