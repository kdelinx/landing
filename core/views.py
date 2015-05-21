#coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from users.models import User
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


def landing(request):
    context = {
        'landing': Landing.objects.all(),
        'userCount': User.objects.all()
    }
    return render(request, 'core/stat.html', context)


def importFromCSV(request):
    pass
    # TODO function for parse VCS