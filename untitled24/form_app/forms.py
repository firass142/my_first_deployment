from django import forms
from django.core import validators
class FormName(forms.Form):
    Full_name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    bot_catcher=forms.CharField(required=Fasle,forms.HiddenInput,validators.MaxLengthValidator(0))