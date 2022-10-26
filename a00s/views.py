from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks
from .models import Image  # import a00s model
from .forms import ImageForm
from mlba_app.models import Page

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse_lazy('login'))
def image_req(request):
    submitted = False
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()
            # compress.showurl(inst.coverimage.url)
            # print (inst.coverimage)
            return HttpResponseRedirect('/a00s/browse/?submitted=True')
    else:
        form = ImageForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'a00s/submitimage.html', {'form': form, 'submitted': submitted})


def edit_req(request, id):
    submitted = False
    my_record = Image.objects.get(id=id)
    form = ImageForm(instance=my_record)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            try:
                inst.user = request.user
            except Exception:
                pass
            inst.save()
            # compress.showurl(inst.coverimage.url)
            # print (inst.coverimage)
            return HttpResponseRedirect('/a00s/browse/?submitted=True')
    else:
        form = ImageForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'a00s/submitimage.html', {'form': form, 'submitted': submitted})


"""
def index(request):
    # imports images and save it in database
    image = Image.objects.all()
    # adding context
    ctx = {'image': image}
    return render(request, 'index.html', ctx)


def upload(request):
    context = dict(backend_form=ImageForm())

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
            return redirect("/a00s/")

    return render(request, 'upload.html', context)
"""


class ImageList(ListView):
    model = Image
    context_object_name = 'all_images'


class ImageDetails(DetailView):
    model = Image
    context_object_name = 'img'


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
