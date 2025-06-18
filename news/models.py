from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class News(models.Model):
    News_title=models.CharField(max_length=100)
    News_desc=HTMLField()
    News_image=models.FileField(upload_to="news/images",max_length=250,null=True,default=None)
    
    news_slug=AutoSlugField(populate_from ="News_title",unique=True,null=True,default=None)
    
    

# Create your models here.
          