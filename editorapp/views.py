from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



from django.contrib.auth.decorators import login_required

from .forms import ArticleForm,CreateuserForm
from .models import Article


from django.http import HttpResponseForbidden
from lock_tokens.exceptions import AlreadyLockedError, UnlockForbiddenError
from lock_tokens.sessions import check_for_session, lock_for_session, unlock_for_session

 
from notifications.signals import notify
from django.db.models.signals import post_save

from notification import views

from datetime import datetime


# Create your views here.
def registation(request):
    if request.user.is_authenticated:
        return redirect('all_post')
    else:    
        form= CreateuserForm()
        if request.method =='POST':
            form=CreateuserForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request,'Account was created for:-'  + user)
                return redirect('login')
        context={'form':form}
        return render(request,'registation.html',context)





def loginpage(request):
    if request.user.is_authenticated:
        return redirect('all_post')
    else:   
        if request.method =='POST':
                username= request.POST.get('username')
                password= request.POST.get('password')
                user=authenticate(request, username=username, password=password)

                if user is not None:
                    login(request,user)
                    return redirect('all_post')
                else:
                    messages.info(request,'username or password is incorrect')    

        context={}
        return render(request,'login.html',context)    




def logoutpage(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def all_post(request):
    allpost= Article.objects.order_by('title')
    return render(request,'allpost.html', {'allpost':allpost})




@login_required(login_url='login')
def add_post(request):
    form=ArticleForm()
    if request.method =="POST":
        form  =ArticleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Successfully Saved', extra_tags='alert')
            
               
            return redirect('all_post')
    else:
        form=ArticleForm()        
    
    return render(request,'post_form.html',{'form':form})



@login_required(login_url='login')
def edit_post(request,slug=None):
    now = datetime.now()
    items= Article.objects.get(slug=slug)
    form =ArticleForm(instance=items)
    user=get_user_model()
    users=User.objects.all()
    p= (now.hour, now.minute, now.second)
    print()
  
    # if request.method =="POST":
    #     form = ArticleForm(request.POST,instance=items)
    #     form.save(commit=True)
    #     return all_post(request)
    try:
        lock_for_session(items, request.session)
        if request.method =="POST":
            form = ArticleForm(request.POST,instance=items)
            form.save(commit=True)
            
            unlock_for_session(items, request.session)
            all_user=users.exclude(id=request.user.id)
            notify.send(request.user, recipient=all_user,  verb="sussess:-   " + f'''<a href="/info/{items.slug}/">{items.title}</a>''')
            messages.success(request, 'Successfully Update', extra_tags='alert')
            return redirect('all_post')
    except AlreadyLockedError:
        return HttpResponseForbidden("This resource is locked, sorry !")

    return render(request,'edit.html',{'form':form}) 
    




@login_required(login_url='login')
def info_post(request,slug=None):
    info= Article.objects.get(slug=slug)
    return render(request,'postinfo.html', {'info':info})


def notificationview(request):
    return render(request,'notification.html')




def deletenotifications(request,id):
    user=get_user_model()
    users=User.objects.all()
    all_user=users.exclude(id=request.user.id)
    notify.send(request.user, recipient=all_user).delete()
   



