from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('This is my first view folder')
def jspider(request):
    return HttpResponse('Welcome to Jspider')
    