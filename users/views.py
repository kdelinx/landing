#coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
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
        'logs': Log.objects.filter(user=user).order_by('id')[:5]
    }
    return render(request, 'users/profile.html', context)


@login_required
def otherProfile(request, id):
    profile = get_object_or_404(User, id=id)
    context = {
        'profile': profile,
        'logs': Log.objects.filter(user=profile.id)[:5]
    }
    return render(request, 'users/profile.html', context)


def register(request):
    pass