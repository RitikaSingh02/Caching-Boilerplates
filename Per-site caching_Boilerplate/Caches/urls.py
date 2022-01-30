from django.contrib import admin
from django.urls import path

from enroll.views import db_based
from file_based_caching.views import file_based

urlpatterns = [
    path('admin/', admin.site.urls),
    path('db_c/' , db_based),# db based caching
    path('file_c/' , file_based),# db based caching

]
