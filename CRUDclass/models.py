from django.db import models
from django.urls import reverse


class Student(models.Model):
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    Scores = models.IntegerField()

    # def det_absolute_url(self):
    #     return reverse("detail", kwargs={"pk": self.pk})
