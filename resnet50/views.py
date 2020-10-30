from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings 

import json
from .forms import UploadFileForm
from .resnet import predict
import os
import glob


# Create your views here.
def index(request):
    prediction = ''
    filename = ''

    if request.method == "POST":
        files = glob.glob('media/images/*')
        for file in files:
            os.remove(file)        

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            filename = request.FILES['image'].name
            prediction = predict(os.path.join(settings.MEDIA_ROOT, f'images/{filename}'))
        return render(request, "resnet50/index.html", {
            'form' : form,
            'prediction' : prediction,
            'img' : os.path.join(settings.MEDIA_URL, f'images/{filename}'),
        })
    else:
        form = UploadFileForm()
    return render(request, "resnet50/index.html", {
        'form' : form,
        'prediction' : prediction,
    })