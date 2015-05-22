#coding: utf-8from django.shortcuts import render, HttpResponseRedirect, get_object_or_404from django.contrib.auth.decorators import login_requiredfrom core.forms import UploadCSVFilefrom django.contrib import messagesfrom users.models import Userfrom core.models import Landingfrom django.core.urlresolvers import reversedef page_404(request):    return render(request, 'core/404.html', {'message': 'Page not found - 404'})def index(request):    if request.user.is_authenticated():        return HttpResponseRedirect(reverse('users:profile'))    return render(request, 'core/index.html')def tos(request):    if request.is_ajax():        return render(request, 'core/ajax_tos.html')    else:        return render(request, 'core/tos.html')def about(request):    return render(request, 'core/about.html')@login_requireddef landing(request):    context = {        'landing': Landing.objects.all(),        'userCount': User.objects.all()    }    return render(request, 'core/stat.html', context)@login_requireddef importFromCSV(request):    if request.POST or request.FILES:        form = UploadCSVFile(request.POST or None, request.FILES or None)        if form.is_valid():            form.save()            messages.success(request, 'File was upload successful.')            return HttpResponseRedirect(                reverse('landing:landing')            )    return render(request, 'core/csv.html')