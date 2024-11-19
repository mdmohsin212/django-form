from django.shortcuts import render
from formapp.forms import *

# Create your views here.

def forms(request):
    if request.method == 'POST':
        form = FormApp(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = FormApp()
    return render(request, 'form.html', {'form' : form})