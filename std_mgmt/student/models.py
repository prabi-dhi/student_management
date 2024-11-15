from django.db import models
from classroom.models import Classroom

class Student(models.Model):
    s_id = models.CharField(max_length=10, primary_key=True)
    s_name = models.TextField(max_length = 50)
    class_enrolled = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="students")
    
    def __str__(self):
        return self.s_name