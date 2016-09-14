from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)


class Talent_managementView(viewsets.ModelViewSet):
    queryset = Talent_management.objects.all()
    serializer_class = Talent_managementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)


class ProductionView(viewsets.ModelViewSet):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)


class EventView(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SongList(viewsets.ModelViewSet):
    model = Songs
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

@csrf_exempt
def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Use the built-in authenticate method to verify
    authenticated_user = authenticate(
            username=req_body['username'],
            password=req_body['password']
            )

    # If authentication was successful, log the user in
    success = True
    if authenticated_user is not None:
        login(request=request, user=authenticated_user)
    else:
        success = False

    data = json.dumps({"success":success})
    return HttpResponse(data, content_type='application/json')
