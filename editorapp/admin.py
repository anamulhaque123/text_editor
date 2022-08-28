from django.contrib import admin
admin.site.site_title ='Document Admin pannel'
admin.site.index_title =''
admin.site.site_header ='Document Admin pannel'
from .models import Article,Comment
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
# admin.site.register(profile)




# admin.site.register(LoggedInUser)