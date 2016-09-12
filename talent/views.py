from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
from talent.serializers import MusiciansSerializer, Talent_managementSerializer, ProductionSerializer, EventSerializer
from talent.models import *

# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the Talent index.")


class MusiciansView(viewsets.ModelViewSet):
    queryset = Musicians.objects.all()
    serializer_class = MusiciansSerializer

class Talent_managementView(viewsets.ModelViewSet):
    queryset = Talent_management.objects.all()
    serializer_class = Talent_managementSerializer

class ProductionView(viewsets.ModelViewSet):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer

class EventView(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
