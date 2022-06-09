from django.db import models
from cloudinary.models import CloudinaryField


class A00(models.Model):
    class Meta:
        db_table = 'a00'

    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class A00Image(models.Model):
    class Meta:
        db_table = 'a00_image'

    a00_tb = models.ForeignKey('A00', related_name='a00_tb', on_delete=models.CASCADE)
    cl_img = CloudinaryField('image', folder="mlba_img/a00s", )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cl_img


class Movie(models.Model):
    class Meta:
        db_table = 'movie'

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Urban(models.Model):
    class Meta:
        db_table = 'urban'

    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UrbanImage(models.Model):
    class Meta:
        db_table = 'urban_image'

    urban_tb = models.ForeignKey('Urban', related_name='urban_tb', on_delete=models.CASCADE)
    cl_img = CloudinaryField('image', folder="mlba_img/urbans", )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cl_img


class UrbanImgMultiple(models.Model):
    class Meta:
        db_table = 'urban_img_multiple'

    urban_image_tb = models.ForeignKey('UrbanImage', related_name='urban_image_tb', on_delete=models.CASCADE)
    cl_img_multiple = CloudinaryField('image', folder="mlba_img/urbans/multiple", )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cl_img


class Resource(models.Model):
    class Meta:
        db_table = 'resource'

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
