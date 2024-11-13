from .models import Student
from student.serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method =='GET':
        students = Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data)     
    if request.method == 'POST':
        serializer = StudentSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
