from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fBasedView(request):
    googleHttpResponse = "<a href=\"https://www.google.com\">Google</a>"
    return HttpResponse(googleHttpResponse)

def buetWeb(request):
    return render(request, "buet.html", {})
