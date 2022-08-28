from django.db import models
from django.utils.text import slugify
from  ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from datetime import datetime    
from django.conf import settings
User= settings.AUTH_USER_MODEL


# from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    slug  =models.SlugField(null=True, blank=True)
    body = RichTextUploadingField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    Is_publise =models.BooleanField(default='',blank=True)
    stay=models.BooleanField(default=False, blank=True)
 
  

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Article,self).save() 




class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

# class LoggedInUser(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='logged_in_user')
#     # Session keys are 32 characters long
#     session_key = models.CharField(max_length=32, null=True, blank=True)

#     def __str__(self):
#         return self.user.username

# class profile(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=150,null=True,blank=True)
#     last_name = models.CharField(max_length=200,blank=True, null=True)
#     phone= models.CharField(max_length=200, null=True,blank=True)

#     def __str__(self):
#          return  str( self.user)

# Model to store the list of logged in users
# class Reciever(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     text = models.TextField()
#     user = models.ManyToManyField(User, through='Article', blank=True, )

#     def __str__(self):
#         return self.created  



# class Sender(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     notificationall = models.ForeignKey(User,on_delete=models.CASCADE)
#     read = models.DateTimeField(null=True, blank=True)



#     def __str__(self):
#         return self.created


      