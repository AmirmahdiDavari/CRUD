from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.


def get_student(request):
    students = StudentModel.objects.all()
    return render(request, 'CURD/student.html', {'students': students})


def create_student(request):
    forms = StudentFormModel()
    if request.method == "POST":
        forms = StudentFormModel(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    return render(request, 'CURD/create_student.html', {"form": forms})

def delete_student(request, student_id):
    student=StudentModel.objects.get(id=student_id)
    student.delete()
    return redirect("/")


def update_Student(request,student_id):
    student=StudentModel.objects.get(id=student_id)
    form=StudentFormModel(instance=student)

    if request.method == "POST":
        form = StudentFormModel(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'CURD/update_student.html', {"form": form})





