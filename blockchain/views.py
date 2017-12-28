from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


#from . import forms

# Create your views here.

def blockchain(request):
    return HttpResponse("<h1>Blockchain page</h1>")

"""
def get_options(request):
    if request.method == 'POST':
        form=BlockchainForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            return HttpResponseRedirect('/thanks/')

    else:
        form = BlockchainForm()
    return render(request, )

"""
