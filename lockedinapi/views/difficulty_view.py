from lockedinapi.models import Difficulty
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status





class DifficultySerializer(serializers.ModelSerializer):
    """JSON serializer for event
    """
    
    class Meta:
        model = Difficulty
        fields = ('id', 'description' )
        depth = 1