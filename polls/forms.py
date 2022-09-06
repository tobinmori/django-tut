from django import forms

class SimpleForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lasstname = forms.CharField(max_length=100)