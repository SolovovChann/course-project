from .models        import product, comment
from django         import forms
from django.forms   import ModelForm, NumberInput, HiddenInput

class commentForm(forms.ModelForm):
    class Meta:
        model   = comment
        fields  = ( 'product', 'rate', 'text' )
        widgets = {
            'product' : HiddenInput(),
            'rate' : NumberInput(attrs={ 'type' : 'range', 'min' : 1, 'max' : 5, 'step' : 1 })
        }