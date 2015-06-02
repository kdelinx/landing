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

class FilterLandingForm(forms.Form):
    domen = forms.CharField(
        label='Domain',
        max_length=255,
    )
    server_path = forms.CharField(
        label='Server path',
        max_length=255,
    )
    link = forms.CharField(
        label='Link URI',
        max_length=255,
    )
    phoneIsPic = forms.BooleanField(
        label='Phone is picture',
        required=True,
    )
    phoneIsText = forms.BooleanField(
        label='Phone is text',
        required=True,
    )
    emailIsPic = forms.BooleanField(
        label='Email is picture',
        required=True,
    )
    emailIsText = forms.BooleanField(
        label='Email is text',
        required=True,
    )
    visit = forms.BooleanField(
        label='Visit',
        required=True,
    )
    visitLink = forms.CharField(
        label='Visit link',
        max_length=255,
    )
    visitDomain = forms.CharField(
        label='Visit domain',
        max_length=255,
    )
    piwik = forms.BooleanField(
        label='Piwik',
        required=True,
    )
    piwikNumber = forms.IntegerField()
    logoId = forms.BooleanField(
        label='Logo id',
        required=True,
    )
    freeAmmount = forms.BooleanField(
        label='freeAmount()',
        required=True,
    )
    bonus = forms.BooleanField(
        label='bonus',
        required=True,
    )
    bonus2 = forms.BooleanField(
        label='bonus2',
        required=True,
    )
    bonus3 = forms.BooleanField(
        label='bonus3',
        required=True,
    )
    currency = forms.BooleanField(
        label='Currency',
        required=True,
    )
    liveChat = forms.BooleanField(
        label='liveChat()',
        required=True,
    )
    serverPathFile = forms.CharField(
        label='Server path file',
        max_length=255,
    )
    regForm = forms.BooleanField(
        label='Register form',
        required=True,
    )
