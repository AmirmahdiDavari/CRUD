from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from . import forms


def templatetext(request):
    return render(request, 'html.html')


def mobiles(request):
    mobiles = {
        "product1": "amir",
        "product2": "davari",
        "product3": "salaim",

    }

    return render(request, '2.html', context=mobiles)


def lap(request):
    lap = {
        "product1": "ali",
        "product2": "aliii",
        "product3": "ahmadi",

    }

    return render(request, '2.html', context=lap)


def pc(request):
    pc = {
        "product1": "abas",
        "product2": "abasi",
        "product3": "abasii",

    }

    return render(request, '2.html', context=pc)


def formsView(request):
    form = forms.ferstformsForm()
    if request.method == 'POST':
        form = forms.ferstformsForm(request.POST)
        if form.is_valid():
            print("name is : ", form.cleaned_data['lname'])

    return render(request, 'form.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def list_projects(request):
    project_list = Project.objects.all()

    return render(request, 'list_projects.html', {'Projects': project_list})


def add_project(request):
    form = ProjectsForm()
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()

            return index(request)



    return render(request, 'add_project.html', {'form': form})
