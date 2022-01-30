from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(30) #time in seconds
def db_based(request):
    return render(request , 'enroll/course.html')

def home(request):
    return render(request , 'enroll/course.html')

# Create your views here.
