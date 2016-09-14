from rest_framework import serializers
from django.contrib.auth.models import User
from talent.models import *

# Turns Python models into JSON and vice versa
class MusiciansSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musicians
        fields = ('url', 'name', 'email', 'phone', 'social', 'genre', 'songs')

class Talent_managementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Talent_management
        fields = ('url', 'name', 'email', 'phone', 'social', 'genre', 'musicians', 'company', 'artistDevelopment')

class ProductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production
        fields = ('url', 'name', 'email', 'phone', 'social', 'genre', 'musicians', 'company', 'engineering')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('url', 'name', 'email', 'phone', 'social', 'genre', 'location')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Songs
        fields = ('owner', 'name', 'email', 'phone', 'social', 'genre', 'location', 'musician')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username')
