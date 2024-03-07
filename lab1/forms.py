from django import forms
from lab1.models import Data

class Studentform(forms.Form):
    username=forms.CharField(max_length=20)
    email=forms.EmailField()
    password = forms.CharField(max_length=20)


class Dataform(forms.ModelForm):
    class Meta:
        model=Data
        fields=['name','track','branch']