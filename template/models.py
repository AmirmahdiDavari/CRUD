from django.db import models


# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    priorety = models.CharField(max_length=128)

    def __str__(self):
        return self.name
