from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    MESSARE ='message'
    APPLICATION= 'application'

    CHOICES=(
        (MESSARE,'Message'),
        (APPLICATION,'Application'))
    to_user= models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="%(class)s_notifications")
    notification_type=models.CharField(max_length=20,choices=CHOICES)
    is_read=models.BooleanField(default=False)
    extra_id=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,null=False, related_name='createnotifications', on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['-created_at']