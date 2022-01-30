from django.contrib import admin
from django.urls import path

from enroll.views import db_based

urlpatterns = [
    path('admin/', admin.site.urls),
    path('db_c/', db_based),
]
