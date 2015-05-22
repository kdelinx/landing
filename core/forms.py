from django.forms import forms
from core.models import Landing


class UploadCSVFile(forms.Form):
    class Meta:
        model = Landing
        fields = ['file']

