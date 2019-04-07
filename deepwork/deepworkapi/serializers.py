from rest_framework import serializers
from deepworkapi.models import Session
from django.contrib.auth.models import User

class SessionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Session
        fields = ('id', 'duration', 'completed', 'owner')

class UserSerializer(serializers.ModelSerializer):
    sessions = serializers.PrimaryKeyRelatedField(many=True, queryset=Session.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'sessions')
