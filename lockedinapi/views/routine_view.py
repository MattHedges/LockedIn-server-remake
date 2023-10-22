from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lockedinapi.models import Routine, ExerciseRoutine, Exercise
from rest_framework.decorators import action
from django.contrib.auth.models import User




class RoutineView(ViewSet):
    """Level up routine view"""

    def retrieve(self, request, pk):
        routine = Routine.objects.get(pk=pk)
        serializer = RoutineSerializer(routine)
        return Response(serializer.data)
    
class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercise
    """
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description1', 'description2', 'description3', 'description4', 'difficulty', 'muscleGroup', 'equipment', 'video' )
    
class ExerciseRoutineSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many=False)

    class Meta:
        model = ExerciseRoutine
        fields = ('exercise', 'id',)

class RoutineSerializer(serializers.ModelSerializer):
    exercise_routine = ExerciseRoutineSerializer(many = True)
    class Meta:
        model = Routine
        fields = ('id','name', 'user', 'exercise_routine', )
        depth = 1