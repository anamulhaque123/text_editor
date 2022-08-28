
from django.urls import path
from .import views
urlpatterns = [
    path('registation/',views.registation, name="registation"),
    path('login/',views.loginpage, name="login"),
    path('logout/',views.logoutpage, name="logout"),
    path('',views.all_post, name="all_post"),
    path('add/post',views.add_post, name='add_post'),
    path('notificationview/',views.notificationview, name='notificationview'),
    path('deletenotifications/<int:id>/',views.deletenotifications, name='deletenotifications'),
    path('info/<slug:slug>/',views.info_post, name = "info"),
    path('edit/post/<slug:slug>/', views.edit_post, name='edit_post'),
]