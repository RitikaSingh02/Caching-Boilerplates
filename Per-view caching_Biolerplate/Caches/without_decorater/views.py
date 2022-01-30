from django.shortcuts import render

def home(request):
    return render(request , 'template/course.html')


# Create your views here.
