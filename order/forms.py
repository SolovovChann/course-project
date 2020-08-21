from .models    import order
from django     import forms
from user.models import UserProfile


class MakeOrderForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['address', 'phone', 'post_index']