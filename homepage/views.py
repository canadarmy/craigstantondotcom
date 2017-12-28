from django.shortcuts import render
from django.apps import apps


# Create your views here.
def home(request):
    all_models = apps.all_models['homepage']
    return render(request, 'homepage.html', {"all_models": all_models})
