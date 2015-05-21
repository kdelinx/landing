from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse


def page_404(request):
    return render(request, 'core/404.html', {'message': 'Page not found - 404'})


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(
            reverse('users:profile')
        )


def tos(request):
    if request.is_ajax():
        return render(request, 'core/ajax_tos.html')
    else:
        return render(request, 'core/tos.html')


def about(request):
    return render(request, 'core/about.html')


def landing(request):
    pass