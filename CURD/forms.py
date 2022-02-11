from django import forms
from .models import *


class StudentFormModel(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
