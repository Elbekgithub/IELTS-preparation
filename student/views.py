from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime

# Create your views here.
from .forms import MockRegisterForm
from teacher.models import MockTest

def mock_list(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    else:
        if not request.user.is_student:
            return redirect('teacher:mock_list')
        else:    
            tests = MockTest.objects.all().order_by('-time_created')
            context = {
                'tests': tests
            }
            return render (request, 'student/mock_list.html', context)

def mock_view(request, slug):
    mock = get_object_or_404(MockTest, slug=slug)
    context = {
        'mock': mock,
    }
    return render (request, 'student/mock_view.html', context)


def mock_register(request,slug):
    mock=get_object_or_404(MockTest,slug=slug)
    user=request.user
    if request.method=='POST':
        form = MockRegisterForm(request.POST or None)
        if form.is_valid():
            mock.registerations.add(user)
            messages.success(request, ' you successfully registered') 
            return redirect('student:mock_view', slug=slug)
    else:
        form = MockRegisterForm()
    return render (request, 'student/mock_view.html', {'form':form})
                            
def my_tests(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    else:
        if not request.user.is_student:
            return redirect('teacher:mock_list')
        else:    
            tests = MockTest.objects.all().order_by('time_start')
            now = datetime.now()
            now
            my_tests = []
            for test in tests:
                if request.user in test.registerations.all():
                    if test.time_start.day >= now.day:
                        my_tests.append(test)
            context = {
                'tests': my_tests,
                'now':now
            }
            return render (request, 'student/my_tests.html', context)

def test_process(request, slug):
    mock = get_object_or_404(MockTest, slug=slug)
    context = {
        'mock':mock
    }
    return render(request, 'student/test_process.html', context)