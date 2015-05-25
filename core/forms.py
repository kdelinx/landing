from django import forms
from core.models import Landing


class UploadCSVFile(forms.ModelForm):
    class Meta:
        model = Landing
        fields = ('fileing',)

class CreateLanding(forms.ModelForm):
    class Meta:
        model = Landing
        fields = ('domen',)
        # TODO other forms
