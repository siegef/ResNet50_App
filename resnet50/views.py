from django.shortcuts import render
from django.http import HttpResponse

from django import forms

class UploadFileForm(forms.Form):
    file = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'custom-file-input'}));

# Create your views here.
def index(request):
    form = UploadFileForm()
    if request.method == "POST":
        form = UploadFileForm(request.POST)
        return render(request, "resnet50/index.html")
    else:
        return render(request, "resnet50/index.html", {
            'form' : form,
        })
