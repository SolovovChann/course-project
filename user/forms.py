from .models                        import UserProfile
from django                         import forms
from django.contrib.auth.models     import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'address', 'phone', 'post_index']