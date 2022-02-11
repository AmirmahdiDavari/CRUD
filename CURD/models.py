from django.db import models

# Create your models here.



class StudentModel(models.Model):
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    Scores = models.IntegerField()