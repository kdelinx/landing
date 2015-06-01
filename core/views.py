# coding: utf-8
import csv
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Log
from users.models import User
from django.db.models import Q
from core.forms import CreateLanding, UploadCSVFile
from django.contrib import messages
from core.models import Landing
from django.core.urlresolvers import reverse


def page_404(request):
    return render(request, 'core/404.html', {'message': 'Page not found - 404'})


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'core/index.html')


def tos(request):
    if request.is_ajax():
        return render(request, 'core/ajax_tos.html')
    else:
        return render(request, 'core/tos.html')


def about(request):
    return render(request, 'core/about.html')


@login_required
def landing(request):
    context = {}
    domain = request.POST.get('domain', '')
    server_path = request.POST.get('serverpath', '')
    link = request.POST.get('phonelink', '')
    phonepic = request.POST.get('phonepic', '')
    phonetext = request.POST.get('phonetext', '')
    emailpic = request.POST.get('emailpic', '')
    emailtext = request.POST.get('emailtext', '')
    visit = request.POST.get('visit', '')
    visitlink = request.POST.get('visitlink', '')
    visitdomain = request.POST.get('visidomain', '')
    piwik = request.POST.get('piwik', '')
    logoid = request.POST.get('logoid', '')
    freeamount = request.POST.get('freeamount', '')
    bonus = request.POST.get('bonus', '')
    bonus2 = request.POST.get('bonus2', '')
    bonus3 = request.POST.get('bonus3', '')
    currency = request.POST.get('currency', '')
    livechat = request.POST.get('livechat', '')
    server_path_file = request.POST.get('serverpathfile', '')
    regform = request.POST.get('regform', '')

    landing = Landing.objects\
        .filter( Q(domen__contains=domain) | Q(server_path__contains=server_path) |
                    Q(link__contains=link) | Q(phoneIsPic=phonepic) |
                  Q(phoneIsText=phonetext) | Q(emailIsPic=emailpic) |
                  Q(emailIsText=emailtext) | Q(visit=visit) |
          Q(visitLink__contains=visitlink) | Q(visitDomain__contains=visitdomain) |
                            Q(piwik=piwik) | Q(logoId=logoid) |
                 Q(freeAmmount=freeamount) | Q(bonus=bonus) |
                          Q(bonus2=bonus2) | Q(bonus3=bonus3) |
                      Q(currency=currency) | Q(liveChat=livechat) |
    Q(serverPathFile__contains=server_path_file) | Q(regForm=regform)
    ).distinct()

    paginator = Paginator(landing, 50)
    page = request.GET.get('page')
    try:
        context['landing'] = paginator.page(page)
    except PageNotAnInteger:
        context['landing'] = paginator.page(1)
    except EmptyPage:
        context['landing'] = paginator.page(paginator.num_pages)

    return render(request, 'core/stat.html', context)


@login_required
def landing_id(request, id):
    current_landing = get_object_or_404(Landing, id=id)
    context = {
        'current_landing': Landing.objects.order_by('-id').filter(id=current_landing.id)
    }
    return render(request, 'core/info.html', context)


@login_required
def landing_delete(request, id):
    landing = get_object_or_404(Landing, id=id)
    user = get_object_or_404(User, id=request.user.id)
    del_log = Log(user=user, log='Delete landing with domen - %s' % landing.domen)
    del_log.save()
    landing.delete()
    messages.error(request, 'Record was deleted!')
    return HttpResponseRedirect(
        reverse('landing:landing')
    )


@login_required
def landing_create(request):
    user = get_object_or_404(User, id=request.user.id)
    name_landing = request.POST.get('domen')
    form = CreateLanding(request.POST or None)
    if form.is_valid():
        form.save()
        new_log = Log(user=user, log='Added new landing with domain - %s' % name_landing)
        new_log.save()
        messages.success(request, 'New landing was added successful!')
        return HttpResponseRedirect(
            reverse('landing:landing')
        )
    return render(request, 'core/add.html', {'form': form})


@login_required
def importFromCSV(request):
    form = UploadCSVFile(request.FILES, request.POST or None)
    if request.POST:
        if form.is_valid():
            obj = form.save()
            csvfile = request.FILES['fileing'].read()
            reader = csv.DictReader(csvfile)
            for domain, serverpath, link, phonepic, phonetext, linkphonepic, emailistext, emailispic, linkemailpic, \
                    visit, visitlink, visitdomain, piwik, piwiknum, logoid, freeamount, bonus, bonus2, bonus3, \
                    currency, livechat, serverpathfile, regform in reader:
                obj.domen = domain
                obj.server_path = serverpath
                obj.link = link
                obj.phoneIsPic = phonepic
                obj.phoneIsText = phonetext
                obj.linkPhonePic = linkphonepic
                obj.emailIsText = emailistext
                obj.emailIsPic = emailispic
                obj.linkEmailPic = linkemailpic
                obj.visit = visit
                obj.visitLink = visitlink
                obj.visitDomain = visitdomain
                obj.piwik = piwik
                obj.piwikNumber = piwiknum
                obj.logoId = logoid
                obj.freeAmmount = freeamount
                obj.bonus = bonus
                obj.bonus2 = bonus2
                obj.bonus3 = bonus3
                obj.currency = currency
                obj.liveChat = livechat
                obj.serverPathFile = serverpathfile
                obj.regForm = regform
                obj.save()
                messages.success(request, 'File was upload successful.')
                return HttpResponseRedirect(
                    reverse('landing:landing')
                )
    return render(request, 'core/csv.html', {'form': form})

