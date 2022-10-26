from django import forms
from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField
from .models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

