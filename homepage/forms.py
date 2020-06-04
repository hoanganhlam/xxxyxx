from django import forms
from .models import Signup

class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
            "type": "email",
            "name": "email",
            "id": "email",
            "size": "150", 
            "placeholder": "Email Address"
        }), label = "")
    class Meta:
        model = Signup
        fields = ('email', )