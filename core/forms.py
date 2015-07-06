from django import forms
from core.models import Landing


class UploadCSVFile(forms.ModelForm):
    class Meta:
        model = Landing
        fields = ('fileing',)


class CreateLanding(forms.ModelForm):
    domen = forms.CharField(
        label='Domain',
        max_length=255,
        required=False,
    )
    server_path = forms.CharField(
        label='Server path',
        max_length=255,
        required=False,
    )
    link = forms.CharField(
        label='Link URI',
        max_length=255,
        required=False,
    )
    phoneIsPic = forms.BooleanField(
        label='Phone is picture',
        required=False,
    )
    phoneIsText = forms.BooleanField(
        label='Phone is text',
        required=False,
    )
    emailIsPic = forms.BooleanField(
        label='Email is picture',
        required=False,
    )
    emailIsText = forms.BooleanField(
        label='Email is text',
        required=False,
    )
    visit = forms.BooleanField(
        label='Visit',
        required=False,
    )
    visitLink = forms.CharField(
        label='Visit link',
        max_length=255,
        required=False,
    )
    visitDomain = forms.CharField(
        label='Visit domain',
        max_length=255,
        required=False,
    )
    piwik = forms.BooleanField(
        label='Piwik',
        required=False,
    )
    piwikNumber = forms.IntegerField(
        required=False,
    )
    logoId = forms.BooleanField(
        label='Logo id',
        required=False,
    )
    freeAmmount = forms.BooleanField(
        label='freeAmount()',
        required=False,
    )
    bonus = forms.BooleanField(
        label='bonus',
        required=False,
    )
    bonus2 = forms.BooleanField(
        label='bonus2',
        required=False,
    )
    bonus3 = forms.BooleanField(
        label='bonus3',
        required=False,
    )
    currency = forms.BooleanField(
        label='Currency',
        required=False,
    )
    affid = forms.BooleanField(
        label='affid',
        required=False
    )
    tracker_id = forms.BooleanField(
        label='tracker_id',
        required=False
    )
    refferer = forms.BooleanField(
        label='refferer',
        required=False
    )
    errors = forms.CharField(
        label='errors',
        max_length=512,
        required=False
    )
    liveChat = forms.BooleanField(
        label='liveChat()',
        required=False,
    )
    serverPathFile = forms.CharField(
        label='Server path file',
        max_length=255,
        required=False,
    )
    regForm = forms.BooleanField(
        label='Register form',
        required=False,
    )

    class Meta:
        model = Landing
        fields = ('domen', 'server_path', 'link', 'phoneIsPic', 'phoneIsText', \
                  'linkPhonePic', 'emailIsPic', 'emailIsText', 'linkEmailPic', \
                  'visit', 'visitLink', 'visitDomain', 'piwik', 'piwikNumber', \
                  'logoId', 'freeAmmount', 'bonus', 'bonus2', 'bonus3', 'currency', \
                  'affid', 'tracker_id', 'refferer', 'liveChat', 'serverPathFile', \
                  'errors', 'regForm',)


class FilterLandingForm(forms.Form):
    link = forms.CharField(
        label='Link URI',
        max_length=255,
        required=False,
    )
    phoneIsPic = forms.BooleanField(
        label='Phone is picture',
        required=False,
    )
    phoneIsText = forms.BooleanField(
        label='Phone is text',
        required=False,
    )
    emailIsPic = forms.BooleanField(
        label='Email is picture',
        required=False,
    )
    emailIsText = forms.BooleanField(
        label='Email is text',
        required=False,
    )
    visit = forms.BooleanField(
        label='Visit',
        required=False,
    )
    visitLink = forms.CharField(
        label='Visit link',
        max_length=255,
        required=False,
    )
    visitDomain = forms.CharField(
        label='Visit domain',
        max_length=255,
        required=False,
    )
    piwik = forms.BooleanField(
        label='Piwik',
        required=False,
    )
    piwikNumber = forms.IntegerField(
        required=False,
    )
    logoId = forms.BooleanField(
        label='Logo id',
        required=False,
    )
    freeAmmount = forms.BooleanField(
        label='freeAmount()',
        required=False,
    )
    bonus = forms.BooleanField(
        label='bonus',
        required=False,
    )
    bonus2 = forms.BooleanField(
        label='bonus2',
        required=False,
    )
    bonus3 = forms.BooleanField(
        label='bonus3',
        required=False,
    )
    currency = forms.BooleanField(
        label='Currency',
        required=False,
    )
    liveChat = forms.BooleanField(
        label='liveChat()',
        required=False,
    )
    affid = forms.BooleanField(
        label='affid',
        required=False
    )
    tracker_id = forms.BooleanField(
        label='tracker_id',
        required=False
    )
    refferer = forms.BooleanField(
        label='refferer',
        required=False
    )
    errors = forms.CharField(
        label='errors',
        max_length=512,
        required=False
    )
    serverPathFile = forms.CharField(
        label='Server path file',
        max_length=255,
        required=False,
    )
    regForm = forms.BooleanField(
        label='Register form',
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(FilterLandingForm, self).__init__(*args, **kwargs)
        domain_value = self.data.get('domen')
        self.fields['domen'] = forms.ChoiceField(choices=[(o['domen'], o['domen']) \
                                    for o in Landing.objects.values('domen').distinct()],
                                                required=False)
        self.fields['server_path'] = forms.ChoiceField(choices=[(i['server_path'], i['server_path']) \
                                    for i in Landing.objects.filter(domen=domain_value).values('server_path')],
                                                       required=False)
