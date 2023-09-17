from django.shortcuts import render
from .models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
        
        data = request.POST

        reciepes_name = data.get('reciepe_name')
        reciepes_description = data.get('reciepe_description')
        
        reciepes_image = request.FILES.get('reciepe_image')

        print(reciepes_name)
        print(reciepes_description)
        print(reciepes_image)
        
    return render(request, "reciepes.html")