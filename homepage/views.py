from django.shortcuts import render
from django.apps import apps


# Create your views here.
def home(request):
    all_models = apps.all_models['homepage']
    context = {
        "all_models": all_models
    }
    return render(request, 'homepage.html', context)
