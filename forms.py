from django import forms
from main.models import User

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("fullname", "bio", "profile_pic")
