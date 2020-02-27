from django.shortcuts import render

# Create your views here.


def teacher(request):
    return render (request, 'teacher/mock_list.html')