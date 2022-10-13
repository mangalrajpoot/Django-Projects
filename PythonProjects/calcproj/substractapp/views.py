from django.shortcuts import render
from django.http import HttpResponse
def substract(request):
    a,b = 100,20
    return HttpResponse("Result is "+str(a-b))
