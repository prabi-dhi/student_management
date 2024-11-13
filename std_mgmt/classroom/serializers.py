from rest_framework import serializers
from classroom.models import Classroom

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['room_number','tot_student']