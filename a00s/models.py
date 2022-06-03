from django.db import models
from cloudinary.models import CloudinaryField


class Image(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    # image field
    image = CloudinaryField('image')
    pub_date = models.DateTimeField(auto_now_add=True)



"""    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
"""
