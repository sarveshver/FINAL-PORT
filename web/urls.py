
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',views.sample,name='mail')

]
urlpatterns += staticfiles_urlpatterns()
