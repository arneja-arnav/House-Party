from rest_framework import serializers
from .models import Room
'''
a Django REST serializer is mandatory for operating on models through the API.
render a Python class to JSON in a browser
so this is for converting the models to json files
and for passing as arguments for the Generic API views

'''

# This is for the Room attributes model for creating Room objects.
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','code','host','guest_can_pause','votes_to_skip','created_at')

#Creating a new Serializer for packaging a POST request to update/create Room
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')
    

