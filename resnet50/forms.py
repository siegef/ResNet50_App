from django import forms
from .models import Upload

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['image']
        widgets = {
            'image' : forms.ClearableFileInput(attrs={'class':'custom-file-input'}),
        }

# class UploadFileForm(forms.Form):
#     file = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'custom-file-input'}), upload_to='images/');

