from django.db import models
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
     #body = models.TextField()
    #body = RichTextField()
    body = RichTextUploadingField()

    def __str__(self):
        return self.title

#class Post(models.Model):
 #   title = models.CharField(max_length=200)
  #  pub_date = models.DateTimeField('date published')
   # body = RichTextUploadingField()
#
 #   def __str__(self):
  #      return self.title