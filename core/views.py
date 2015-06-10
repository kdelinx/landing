# coding: utf-8
import csv
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Log
from users.models import User
from core.forms import CreateLanding, UploadCSVFile, FilterLandingForm
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
    context = {
        'landing_filter_form': FilterLandingForm(initial=request.POST)
    }
    if request.method == 'POST':
        filter_params = {}
        form = FilterLandingForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.iteritems():
                if name not in form.data:
                    continue

                if value != '' and value is not None:
                    if name in ('domen', 'server_path', 'link', 'visitLink', 'visitDomain', 'serverPathFile'):
                        filter_params[name + '__icontains'] = value
                    else:
                        filter_params[name] = value

            landing = Landing.objects.filter(**filter_params)
        else:
            landing = Landing.objects.all()
    else:
        landing = Landing.objects.all()

    page = request.GET.get('page', '1')
    paginator = Paginator(landing, 50)
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
    else:
        print form.errors
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


@login_required
def landing_full(request):
    context = {
        'landing_filter_form': FilterLandingForm(initial=request.POST)
    }
    if request.method == 'POST':
        filter_params = {}
        form = FilterLandingForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.iteritems():
                if name not in form.data:
                    continue

                if value != '' and value is not None:
                    if name in ('domen', 'server_path', 'link', 'visitLink', 'visitDomain', 'serverPathFile'):
                        filter_params[name + '__icontains'] = value
                    else:
                        filter_params[name] = value

            context['landing'] = Landing.objects.filter(**filter_params)
        else:
            context['landing'] = Landing.objects.all()
    else:
        context['landing'] = Landing.objects.all()

    return render(request, 'core/full.html', context)
