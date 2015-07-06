# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from core.models import Landing, Log
from users.models import User
from users.forms import UserCreateForm
from django.db.models import Count, Sum
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext


@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    context = {
        'profile': user,
        'logs': Log.objects.filter(user=user).order_by('-id')[:5]
    }
    return render(request, 'users/profile.html', context)


@login_required
def otherProfile(request, id):
    profile = get_object_or_404(User, id=id)
    context = {
        'profile': profile,
        'logs': Log.objects.filter(user=profile.id)[:5],
    }
    return render(request, 'users/profile.html', context)


def register(request, template_name='users/register.html',
             form=UserCreateForm, autologin=True):
    form = form(request.POST or None)
    if form.is_valid():
        form.save()
        if autologin:
            username = form.cleaned_data['login']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Successful! You are a new user!')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            return HttpResponseRedirect(reverse('index'))
    return render(request, template_name, {'form': form})
