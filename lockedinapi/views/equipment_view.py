from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lockedinapi.models import Equipment
from rest_framework.decorators import action

class EquipmentView(ViewSet):
    """Level up event view"""

    def retrieve(self, request, pk):
        equipment = Equipment.objects.get(pk=pk)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data, status=status.HTTP_200_OK)




class EquipmentSerializer(serializers.ModelSerializer):
    """JSON serializer for event
    """
    
    class Meta:
        model = Equipment
        fields = ('id', 'name' )
        depth = 1