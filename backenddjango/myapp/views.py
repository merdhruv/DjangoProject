from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    peoples = [
    {'name':'dhruv','age':22},
    {'name':'divyam','age':22},
    {'name':'ayush','age':21},
    {'name':'abhinav','age':17}
]

    # text = """
    #     Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    # """

    vegetables = ['pumpkin','tomato','potato']

    return render(request, "index.html", context = {'peoples': peoples, 'vegetables':vegetables, 'page':"Django Project"})

def about(request):
    context = {'page': 'About'}
    return render(request, "about.html", context )
    
def contact(request):
    context = {'page':'Contacts'}
    return render(request, "contact.html", context)