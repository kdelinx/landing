#coding: utf-8
import csv
import uuid
from django.db import models
from users.models import User
from django.utils.translation import ugettext_lazy as _


def pathToCSV(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'csv/%s%s%s' % (filename[:1], filename[2:5], filename)

class Landing(models.Model):
    file = models.FileField(
        _('Upload file'),
        upload_to=pathToCSV,
        blank=True,
        null=True,
    )
    domen = models.CharField(
        _('Domain'),
        max_length=255,
    )
    server_path = models.CharField(
        _('Server path'),
        max_length=255,
    )
    link = models.URLField(
        _('Link path'),
        blank=False,
        null=False,
        max_length=255,
    )
    phoneIsPic = models.BooleanField(
        _('Phone as picture'),
        default=False,
    )
    phoneIsText = models.BooleanField(
        _('Phone as text'),
        default=False,
    )
    linkPhonePic = models.URLField(
        _('Phone link'),
        null=True,
        blank=True,
        max_length=255,
    )
    emailIsPic = models.BooleanField(
        _('Email is picture'),
        default=False,
    )
    emailIsText = models.BooleanField(
        _('Email is text'),
        default=False,
    )
    linkEmailPic = models.URLField(
        _('Email picture link'),
        null=True,
        blank=True,
        max_length=255,
    )
    visit = models.BooleanField(
        _('Visit state'),
        default=False,
    )
    visitLink = models.CharField(
        _('Domain for visit'),
        max_length=150,
    )
    visitDomain = models.CharField(
        _('Domain visit from coockie'),
        max_length=125,
    )
    piwik = models.BooleanField(
        default=False,
    )
    piwikNumber = models.SmallIntegerField(
        _('Number of piwik'),
        default=0,
    )
    logoId = models.BooleanField(
        _('Logo ID'),
        default=False,
    )
    freeAmmount = models.BooleanField(
        _('Free ammount field'),
        default=False,
    )
    bonus = models.BooleanField(
        _('Bonus'),
        default=False,
    )
    bonus2 = models.BooleanField(
        _('Bonus2'),
        default=False,
    )
    bonus3 = models.BooleanField(
        _('Bonus3'),
        default=False,
    )
    currency = models.BooleanField(
        _('Currency'),
        default=False,
    )
    liveChat = models.BooleanField(
        _('Live chat function'),
        default=False,
    )
    serverPathFile = models.CharField(
        _('Server file path'),
        max_length=255,
    )
    regForm = models.BooleanField(
        _('Registration forms'),
        default=False,
    )

    class Meta:
        verbose_name = _('Landing')
        verbose_name_plural = _('Landings')

    def __unicode__(self):
        return _('%s - %s' % (self.domen, self.serverPathFile))

    def save(self, *args):
        with open(self.file, 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for domain, serverpath, link, phonepic, phonetext, linkphonepic, emailistext, emailispic, linkemailpic, \
                    visit, visitlink, visitdomain, piwik, piwiknum, logoid, freeamount, bonus, bonus2, bonus3, \
                    currency, livechat, serverpathfile, regform, files in reader:
                self.file = files
                self.domen = domain
                self.server_path = serverpath
                self.link = link
                self.phoneIsPic = phonepic
                self.phoneIsText = phonetext
                self.linkPhonePic = linkphonepic
                self.emailIsText = emailistext
                self.emailIsPic = emailispic
                self.linkEmailPic = linkemailpic
                self.visit = visit
                self.visitLink = visitlink
                self.visitDomain = visitdomain
                self.piwik = piwik
                self.piwikNumber = piwiknum
                self.logoId = logoid
                self.freeAmmount = freeamount
                self.bonus = bonus
                self.bonus2 = bonus2
                self.bonus3 = bonus3
                self.currency = currency
                self.liveChat = livechat
                self.serverPathFile = serverpathfile
                self.regForm = regform
        super(Landing, self).save(*args)


class Log(models.Model):
    user = models.ForeignKey(User)
    log = models.TextField(
        _('Action listing'),
    )

    class Meta:
        verbose_name = _('Logging')
        verbose_name_plural = _('Loggings')

    def __unicode__(self):
        return self.user
