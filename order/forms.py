from .models        import order
from django         import forms

class orderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ( 'fio', 'phone', 'email', 'address' )