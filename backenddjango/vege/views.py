from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
        
        data = request.POST

        reciepes_name = data.get('reciepe_name')
        reciepes_description = data.get('reciepe_description')
        
        reciepes_image = request.FILES.get('reciepe_image')

        Reciepe.objects.create(
        reciepe_name = reciepes_name,
        reciepe_description = reciepes_description,
        reciepe_image = reciepes_image,
        )
        return redirect('/reciepes/')

    queryset = Reciepe.objects.all()
    context = {'reciepes' : queryset}

    return render(request, "reciepes.html" , context)

def delete_reciepe(request, id):
    queryset = Reciepe.objects.get(id = id)
    queryset.delete();
    return redirect ('/reciepes/')