from django import forms
import datetime

YEAR_CHOISE = ['2004', '2005', '2006', '2007']
COLORS = [('b', 'Blue'),
    ('g', 'Green'),
    ('w', 'White'),]
class FormApp(forms.Form):
    name = forms.CharField(max_length=30, initial='Mohsin')
    roll = forms.IntegerField()
    email = forms.EmailField(required=False, label='Enter your email')
    about = forms.CharField(widget=forms.Textarea(attrs={'rows' : 4})) # Deafult 10
    
    date = forms.DateField(widget=forms.NumberInput(attrs={'type' : 'date'}), initial=datetime.date.today)
    
    choise_year = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOISE))
    value = forms.DecimalField()
    
    favorite_color = forms.ChoiceField(choices=COLORS)
    
    color = forms.ChoiceField(widget=forms.RadioSelect, choices=COLORS)
    
    my_color = forms.MultipleChoiceField(choices=COLORS)
    
    agree = forms.BooleanField(initial=False)