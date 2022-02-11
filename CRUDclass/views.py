from pyexpat import model

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student


# Create your views here.
class StudentListView(ListView):
    model = Student
    # template_name="default {model class name}}_list.html"
    template_name = "CRUDclass/student_list.html"
    context_object_name = "Student_list"


class StudentDetailView(DetailView):
    model = Student
    # template_name="default {model class name}_detail.html"
    template_name = "CRUDclass/studentmodel_detail.html"
    context_object_name = "studentmodel"


class StudentCreateView(CreateView):
    model = Student
    fields = ('fname', 'lname', 'Scores')
    # template_name="default {model class name}_form.html"
    template_name = "CRUDclass/studentmodel_form.html"
    success_url = "/crud/list"


class StudentUpdateView(UpdateView):
    model = Student
    fields = ("fname", "lname")
    template_name = "CRUDclass/studentmodel_form.html"
    success_url =  reverse_lazy("student")





class  StudentdeleteView (DeleteView):
    model = Student
    # template_name="default {model class name}_confirm_delete.html"
    template_name="CRUDclass/student_confirm_delete.html"

    success_url = reverse_lazy("student")

