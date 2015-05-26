from django import forms
from core.models import Landing


class UploadCSVFile(forms.ModelForm):
    class Meta:
        model = Landing
        fields = ('fileing',)

class CreateLanding(forms.ModelForm):
    class Meta:
        model = Landing
        fields = ('domen', 'server_path', 'link', 'phoneIsPic', 'phoneIsText', \
                  'linkPhonePic', 'emailIsPic', 'emailIsText', 'linkEmailPic', \
                  'visit', 'visitLink', 'visitDomain', 'piwik', 'piwikNumber', \
                  'logoId', 'freeAmmount', 'bonus', 'bonus2', 'bonus3', 'currency', \
                  'liveChat', 'serverPathFile', 'regForm',)
