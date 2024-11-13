from rest_framework import serializers
from .models import Teacher

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name','subject','class_assigned']