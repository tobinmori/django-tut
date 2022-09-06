from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="name")
    email = forms.CharField(max_length=100, label="email")

def contact(request):
    print("CONTACT")
    submitted=False
    if request.method=="POST":
        form=ContactForm(request.POST)
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'contact/contact.html', {'form':form, 'submitted':submitted})