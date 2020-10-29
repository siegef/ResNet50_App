from django.urls import path

from . import views

app_name = 'resnet50'
urlpatterns = [
    path("", views.index, name="index")
]
