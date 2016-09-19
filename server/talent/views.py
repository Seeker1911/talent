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
from talent.serializers import *
from talent.models import *

# from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the Talent index.")


class MusiciansView(viewsets.ModelViewSet):
    queryset = Musicians.objects.all()
    serializer_class = MusiciansSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class Talent_managementView(viewsets.ModelViewSet):
#     queryset = Talent_management.objects.all()
#     serializer_class = Talent_managementSerializer
#
#
# class ProductionView(viewsets.ModelViewSet):
#     queryset = Production.objects.all()
#     serializer_class = ProductionSerializer


class EventView(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

class SongView(viewsets.ModelViewSet):
    model = Song
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

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

@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    email=req_body['email'],
                    first_name=req_body['first_name'],
                    last_name=req_body['last_name'],
                    )

    new_user.musicians.phone=req_body.get('phone', None)
    new_user.musicians.social=req_body.get('social', None)
    new_user.musicians.genre=req_body.get('genre', None)
    new_user.musicians.company=req_body.get('company', None)
    new_user.musicians.engineering=req_body.get('engineering', False)
    new_user.musicians.artistDevelopment=req_body.get('artistDevelopment', False)
    new_user.musicians.bio=req_body.get('bio', None)
    new_user.musicians.location=req_body.get('location', None)


    # Commit the user to the database by saving it
    new_user.save()

    return login_user(request)
