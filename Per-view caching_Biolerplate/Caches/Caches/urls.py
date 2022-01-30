import imp
from django.contrib import admin
from django.urls import path

from enroll.views import db_based 
from without_decorater.views import home

#for using same function with caching capability at one uri and no caching at the other uri
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('db_c/', db_based),


    path('', home),
    path('home/' , cache_page(60)(home))

]
