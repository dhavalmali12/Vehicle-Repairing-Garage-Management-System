from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    News_title=models.CharField(max_length=100)
    News_desc=HTMLField()
    

# Create your models here.
