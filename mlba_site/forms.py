from django import forms
from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField
from .models import *


class A00Form(ModelForm):
    class Meta:
        model = A00
        fields = '__all__'

        widgets = {
            'desc': forms.Textarea(attrs={'rows': 3}),
        }


class A00ImgForm(ModelForm):
    class Meta:
        model = A00Image
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['a00_tb'].widget = forms.HiddenInput()


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        widgets = {
            'desc': forms.Textarea(attrs={'rows': 3}),
        }


class UrbanForm(ModelForm):
    class Meta:
        model = Urban
        fields = '__all__'

        widgets = {
            'desc': forms.Textarea(attrs={'rows': 3}),
        }


class UrbanImgForm(ModelForm):
    class Meta:
        model = UrbanImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['urban_tb'].widget = forms.HiddenInput()


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

        widgets = {
            'desc': forms.Textarea(attrs={'rows': 3}),
        }
