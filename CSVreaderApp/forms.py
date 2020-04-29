from django import forms

class uploadfile(forms.Form):
    file = forms.FileField(label = "Input File")