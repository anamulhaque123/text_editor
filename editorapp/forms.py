from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article


class ArticleForm(ModelForm):
     class Meta:
         model= Article
         fields = '__all__'


class CreateuserForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2']
