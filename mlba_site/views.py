import cloudinary.uploader
from django.shortcuts import render, redirect
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks
from flask.ctx import RequestContext

from .models import *
from .forms import *
from mlba_app.models import Page

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required


# ::::::: A00s
# @login_required(login_url=reverse_lazy('login'))
def create_a00(request):
    submitted = False
    if request.method == 'POST':
        form = A00Form(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()

            the_id = (A00.objects.last()).id

            return HttpResponseRedirect('/create_a00_img/' + str(the_id))
    else:
        form = A00Form()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'a00s/create_a00.html', {'form': form, 'submitted': submitted})


def view_a00(request, pk):
    template_name = "a00s/view_a00.html"
    # dictionary for initial data with
    # field names as keys
    a00_data = A00.objects.get(id=pk)
    if A00Image.objects.filter(a00_tb=pk):
        img = A00Image.objects.get(a00_tb=pk)
        print("Myoutput", img.cl_img)
    else:
        img = ''

    # add the dictionary during initialization

    return render(request, template_name, {'a00_data': a00_data, 'img': img})


def edit_a00(request, pk):
    template_name = "a00s/edit_a00.html"
    context = {}

    obj = get_object_or_404(A00, id=pk)
    if A00Image.objects.filter(a00_tb=pk):
        img_obj = A00Image.objects.get(a00_tb=pk)
        print("Myoutput", img_obj.cl_img)
    else:
        img_obj = pk

    form = A00Form(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()  # commit=False)
        return HttpResponseRedirect('/view_a00/' + str(pk))
    # add form dictionary to context
    context["form", 'img_obj'] = form
    # context['img_obj'] = img_obj

    return render(request, template_name, context)


def delete_a00(id):
    img = get_object_or_404(A00Image, a00_tb=id)

    cloudinary.uploader.destroy(img.cl_img.public_id, invalidate=True)
    if img != '':
        img.delete()

        return HttpResponseRedirect("/list_a00s/")
        success_message = "Item %(name)s deleted successfully"
    else:
        return HttpResponseRedirect("/view_a00/" + str(id))


def list_a00s(request):
    context = {}
    # a00_i = A00Img
    all_a00s = A00Image.objects.all().prefetch_related("a00_tb")  # A00.objects.select_related()
    template = 'a00s/list_a00s.html'
    context['all_a00s'] = all_a00s

    # add the dictionary during initialization
    return render(request, template, context)


# ::::::: A00Image
# @login_required(login_url=reverse_lazy('login'))
def create_a00_img(request, a00_id):
    template_name = 'a00_imgs/create_a00_img.html'
    context = {}
    initial_dict = {
        "a00_tb": a00_id,
    }

    form = A00ImgForm(request.POST or None, initial=initial_dict)
    if request.method == 'POST':
        form = A00ImgForm(request.POST, request.FILES)
        if form.is_valid():

            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()

            return HttpResponseRedirect('/view_a00/' + str(a00_id))
    context['form'] = form
    return render(request, template_name, context)


def delete_a00_img(request, a00_id):
    img = get_object_or_404(A00Image, a00_tb=a00_id)

    if a00_id != '':
        cloudinary.uploader.destroy(img.cl_img.public_id, invalidate=True)
        img.delete()

        return HttpResponseRedirect("/list_a00s/")

    else:
        return HttpResponseRedirect("/view_a00/" + str(id))

    print('WhatIds', a00_id)


# ::::::: Movie

@login_required(login_url=reverse_lazy('login'))
def create_movie(request):
    submitted = False
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()

            return HttpResponseRedirect('/list_movies/?submitted=True')
    else:
        form = MovieForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'movies/create_movie.html', {'form': form, 'submitted': submitted})


def view_movie(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {"data": Movie.objects.get(id=id)}

    # add the dictionary during initialization

    return render(request, "movies/view_movie.html", context)


def edit_movie(request, id):
    submitted = False
    obj = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = MovieForm(request.POST or None, instance=obj)
        if form.is_valid():
            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()
            return HttpResponseRedirect('/view_movie/' + id)
    else:
        form = MovieForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'movies/edit_movie.html', {'form': form, 'submitted': submitted})


def delete_movie(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Movie, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "movies/delete_movie.html", context)


def list_movies(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["all_movies"] = Movie.objects.all()

    return render(request, "movies/list_movies.html", context)


# ::::::: Urban

# @login_required(login_url=reverse_lazy('login'))
def create_urban(request):
    submitted = False
    if request.method == 'POST':
        form = UrbanForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()

            the_id = (Urban.objects.last()).id

            return HttpResponseRedirect('/create_urban_img/' + str(the_id))
    else:
        form = UrbanForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'urbans/create_urban.html', {'form': form, 'submitted': submitted})


def view_urban(request, pk):
    # dictionary for initial data with
    # field names as keys
    urban_data = Urban.objects.get(id=pk)
    img = UrbanImage.objects.get(urban_tb=pk)
    ig = UrbanImgMultiple.objects.filter(urban_i_m_tb=pk)
    if ig != "":
        img_multiple = urban_data.urban_i_m_tb.all()
    else:
        img_multiple = pk
        print('NODATA FOUND')

    # add the dictionary during initialization

    return render(request, "urbans/view_urban.html",
                  {'urban_data': urban_data, 'img': img, 'img_multiple': img_multiple})


def edit_urban(request, pk):
    template_name = "urbans/edit_urban.html"
    context = {}
    obj = get_object_or_404(Urban, id=pk)
    if UrbanImage.objects.filter(urban_tb=pk):
        img_obj = UrbanImage.objects.get(urban_tb=pk)
        print("Myoutput", img_obj.cl_img)
    else:
        img_obj = pk

    form = UrbanForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/view_urban/' + str(pk))

    # add form dictionary to context
    context["form"] = form
    context['img_obj'] = img_obj

    return render(request, template_name, context)


def delete_urban(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Urban, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "urbans/delete_urban.html", context)


def list_urbans(request):
    context = {}

    all_urbans = UrbanImage.objects.all().prefetch_related("urban_tb")
    template = 'urbans/list_urbans.html'
    context['all_urbans'] = all_urbans

    # add the dictionary during initialization
    return render(request, template, context)


# ::::::: UrbanImage
# @login_required(login_url=reverse_lazy('login'))
def create_urban_img(request, urban_id=None):
    template_name = 'urban_imgs/create_urban_img.html'
    context = {}
    initial_dict = {
        "urban_tb": urban_id,
    }

    form = UrbanImgForm(request.POST or None, initial=initial_dict)
    if request.method == "POST":
        form = UrbanImgForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()

            return HttpResponseRedirect('/view_urban/' + str(urban_id))
    context['form'] = form
    return render(request, template_name, context)


def delete_urban_img(request, urban_id):
    img = get_object_or_404(UrbanImage, urban_tb=urban_id)

    if urban_id != '':
        cloudinary.uploader.destroy(img.cl_img.public_id, invalidate=True)
        img.delete()

        return HttpResponseRedirect("/list_urbans/")

    else:
        return HttpResponseRedirect("/view_urban/" + str(urban_id))

    print('WhatIds', urban_id)


# ::::::: UrbanImagesMultiple
# @login_required(login_url=reverse_lazy('login'))
def create_u_i_m(request, urban_id=None):
    template_name = 'urban_imgs_multiple/create_u_i_m.html'
    context = {}
    initial_dict = {
        "urban_i_m_tb": urban_id,
    }

    form = UrbanImgMultipleForm(request.POST or None, initial=initial_dict)
    if request.method == "POST":
        form = UrbanImgMultipleForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()

            return HttpResponseRedirect('/view_urban/' + str(urban_id))
    context['form'] = form
    return render(request, template_name, context)


def delete_u_i_m(request, pk, urban_id):
    img = get_object_or_404(UrbanImgMultiple, id=pk)

    if id != '':
        cloudinary.uploader.destroy(img.cl_img_multiple.public_id, invalidate=True)
        img.delete()

        return HttpResponseRedirect("/list_urbans/")

    else:
        return HttpResponseRedirect("/view_urban/" + str(urban_id))

    print('WhatIds', urban_id)


""" ::::::: Resource """


@login_required(login_url=reverse_lazy('login'))
def create_resource(request):
    submitted = False
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()

            return HttpResponseRedirect('/list_resources/?submitted=True')
    else:
        form = ResourceForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'resources/create_resource.html', {'form': form, 'submitted': submitted})


def view_resource(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {"data": Resource.objects.get(id=pk)}

    # add the dictionary during initialization

    return render(request, "resources/view_resource.html", context)


def edit_resource(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Resource, id=pk)

    # pass the object as instance in form
    form = ResourceForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/view_resource/' + str(pk))

    # add form dictionary to context
    context["form"] = form

    return render(request, 'resources/edit_resource.html', context)


def delete_resource(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Resource, id=pk)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_resource.html", context)


def list_resources(request):
    # dictionary for initial data with
    # field names as keys
    context = {"all_resources": Resource.objects.all()}

    # add the dictionary during initialization

    return render(request, "resources/list_resources.html", context)


""" User Registration ::::::: """


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
