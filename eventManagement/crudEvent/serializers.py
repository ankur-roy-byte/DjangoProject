from django.contrib.auth.models import User, Group
from rest_framework import serializers

from eventManagement.crudEvent.models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'published', 'totalPerson', 'release_date', 'event_size']