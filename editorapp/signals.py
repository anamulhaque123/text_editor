from django.db.models.signals import post_save
from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib.auth.models import User
# from .models  import  LoggedInUser
from .models  import  profile




@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
        print("profile created.")
# post_save.connect(create_profile, sender=User)        



@receiver(post_save, sender=User)
def update_profile(sender,instance,created, **kwargs):

    if created == False:
        instance.profile.save()
        print("profile update")
# post_save.connect(update_profile, sender=User)      




# @receiver(user_logged_in)
# def on_user_logged_in(sender, request, **kwargs):
#     LoggedInUser.objects.get_or_create(user=kwargs.get('user')) 


# @receiver(user_logged_out)
# def on_user_logged_out(sender, **kwargs):
#     LoggedInUser.objects.filter(user=kwargs.get('user')).delete()
