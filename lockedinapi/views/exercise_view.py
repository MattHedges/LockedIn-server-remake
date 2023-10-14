from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lockedinapi.models import Exercise, Difficulty, MuscleGroup, Equipment
from rest_framework.decorators import action


class ExerciseView(ViewSet):
    """Level up exercise view"""

    def retrieve(self, request, pk):
        exercise = Exercise.objects.get(pk=pk)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercise
    """
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description1', 'description2', 'description3', 'description4', 'difficulty', 'muscleGroup', 'equipment', 'video' )
        depth = 1