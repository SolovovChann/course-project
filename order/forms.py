from .models import order
from django         import forms
from django.forms   import ModelForm, NumberInput

class orderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ( "fio" , "address" )