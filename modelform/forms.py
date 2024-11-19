from django import forms
from modelform.models import ModelForm

class FormModel(forms.ModelForm):
    class Meta:
        model = ModelForm
        fields = '__all__'