import form as form
from django.shortcuts import render
from .forms import *
# Create your views here.




def index(request):
    return render(request,'sessione/card.html',)



def displycard(request):
    return render(request,'sessione/displycard.html')


def addcard(request):
    form=ItemForm()

    if request.method == 'POST':
        name = request.POST['name']
        quality = request.POST['quality']
        request.session[name]= quality
    return render(request, 'sessione/addcard.html',{"form":form})


