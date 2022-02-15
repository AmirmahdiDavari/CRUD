from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def pagecounter(request):
    count =request.session.get("count",1)
    count= count+1
    request.session['count']=count
    return render(request,'sessione/counter.html',{"count":count})

