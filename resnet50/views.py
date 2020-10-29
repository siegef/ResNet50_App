from django.shortcuts import render,redirect
from django.http import HttpResponse

import json
from .forms import UploadFileForm

# Create your views here.
def index(request):
    prediction = 'Doggo'
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        # print(request.FILES)
        # print(form) 
        if form.is_valid():
            # print("Valid form")
            form.save()
        # return redirect ("resnet50:success")
        # return render(request, "resnet50/index.html")
    else:
        form = UploadFileForm()
    return render(request, "resnet50/index.html", {
        'form' : form,
        'prediction' : prediction,
    })