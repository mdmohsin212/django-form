from django.shortcuts import render
from modelform.forms import FormModel

# Create your views here.

def ModelPage(request):
    form = FormModel()
    return render(request, 'model_form.html', {'form' : form})