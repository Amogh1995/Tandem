from django import forms

from models import UploadFile
from models import UploadFile1

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile


class UploadFileForm1(forms.ModelForm):
    class Meta:
        model = UploadFile1
