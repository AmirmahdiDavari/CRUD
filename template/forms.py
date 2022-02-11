from django import forms
from .models import Project

from template.models import Project


class ferstformsForm(forms.Form):
    name = forms.IntegerField()
    lname = forms.CharField()
    fname = forms.CharField()


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
