import os
from mlba import settings
from django.shortcuts import render
from django.contrib.staticfiles.urls import static
from django.http import HttpResponse
from mlba_app.models import Page


def index(request, pagename):
    path = settings.MEDIA_ROOT
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    imgs = os.listdir(path + '/images')
    vid = os.listdir(path + '/video')
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'images': imgs,
        'videos': vid,
    }

    # return HttpResponse("<h1> Homepage </h1>")
    # return render(request,'base.html')
    return render(request, 'mlba_app/mlba_app.html', context)


def about(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
    }
    # return HttpResponse("<h1> Homepage </h1>")
    # return render(request,'base.html')
    return render(request, 'mlba_app/mlba_app.html', context)