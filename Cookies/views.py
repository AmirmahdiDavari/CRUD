from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>start server Cookies</h1>")


def abut(request):
    if request.session.test_cookie_worked():
        print("cookoes worked")
    request.session.delete_test_cookie()
    return HttpResponse("<h1>abut server Cookies</h1>")


def countviews(request):
    if "count" in request.COOKIES:
        count = int(request.COOKIES["count"])+1
    else:
        count = 1
    response = render(request,"cookies/count.html",{'count':count})
    response.set_cookie('count', count)
    return response

