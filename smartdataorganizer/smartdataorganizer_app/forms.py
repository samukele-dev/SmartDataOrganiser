# smartdataorganizer_app/forms.py
from django import forms
from .models import Spreadsheet

class UploadForm(forms.ModelForm):
    class Meta:
        model = Spreadsheet
        fields = ['file']

class FilterForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)  # Add more fields as needed
