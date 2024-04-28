from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['minlength'] = 3
        self.fields['password2'].widget.attrs['minlength'] = 3

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 3:
            raise forms.ValidationError("Password must be at least 3 characters long.")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        if len(password2) < 3:
            raise forms.ValidationError("Password must be at least 3 characters long.")
        return password2

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
