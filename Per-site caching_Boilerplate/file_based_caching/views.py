from django.shortcuts import render

def file_based(request):
    return render(request , 'file_based/course.html')
# Create your views here.
