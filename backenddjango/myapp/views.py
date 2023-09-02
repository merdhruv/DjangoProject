from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

peoples = [
    {'name':'dhruv','age':22},
    {'name':'divyam','age':22},
    {'name':'ayush','age':21},
    {'name':'abhinav','age':17}
]

def index(request):
    return render(request, "index.html", context = {'peoples': peoples})

def about(request):
    return render(request, "about.html")