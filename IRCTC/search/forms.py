from django import forms

class trainSearchForm(forms.Form):
    source = forms.CharField(max_length=20)
    destination = forms.CharField(max_length=20)