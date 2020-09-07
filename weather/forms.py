from django.forms import ModelForm, TextInput
from .models import Member


class UserForm(ModelForm):
    class Meta:
        model = Member
        fields = {'Name','Username','Password1','Password2','DOB'}
        widgets = {'Name': TextInput(attrs={'placeholder': 'Enter Name'})}