from django.db import models

class Class(models.Model):
    room = models.CharField(max_length=20)
    tot_student = models.CharField(max_length = 5)