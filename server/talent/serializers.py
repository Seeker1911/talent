from rest_framework import serializers
from django.contrib.auth.models import User
from talent.models import *

# Turns Python models into JSON and vice versa
class MusiciansSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musicians
        fields = ('url', 'phone', 'social', 'genre', 'songs', 'company', 'engineering', 'artistDevelopment', 'bio', 'location')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name')
# class Talent_managementSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Talent_management
#         fields = ('url', 'username', 'user_id', 'email', 'phone', 'social', 'genre', 'artists', 'company', 'artistDevelopment')
#
# class ProductionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Production
#         fields = ('url', 'username', 'user_id', 'email', 'phone', 'social', 'genre', 'artists', 'company', 'engineering')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('url', 'name', 'email', 'phone', 'social', 'genre', 'location')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('artist', 'title', 'genre', 'length')
