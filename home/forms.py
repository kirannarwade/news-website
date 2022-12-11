from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        lables = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'})}

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email  

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError("An user with this username already exists!")
        return username  
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


    # def clean_username(self):
    #     data = self.cleaned_data['username']
    #     if not data:
    #         raise forms.ValidationError("Please Enter Username.")
    #     return data
       
        

    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if not password:
    #         raise forms.ValidationError("Please Enter Password.")
    #     return password


    # def clean(self):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     try:
    #         User.objects.get(username=username, password=password)
    #     except User.DoesNotExist:
    #         raise forms.ValidationError("Email or Password is incorrect.")
    #     return self.cleaned_data


