from .models import Classroom
from classroom.serializers import ClassSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def classroom_list(request):
    if request.method =='GET':
        classrooms = Classroom.objects.all()
        serializer=ClassSerializer(classrooms, many=True)
        return Response(serializer.data)     
    if request.method == 'POST':
        serializer = ClassSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
