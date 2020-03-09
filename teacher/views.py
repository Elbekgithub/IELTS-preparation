from django.shortcuts import render, get_object_or_404, redirect

from .models import MockTest, Listening, Reading, Writing, Speaking, AnswerListening, AnswerReading
from accounts.models import Teacher
from .forms import (NewMockForm, 
                    ListeningForm, 
                    ReadingForm, 
                    WritingForm, 
                    SpeakingForm, 
                    AnswerListeningForm, 
                    AnswerReadingForm, 
                    AnswerListeningUpdateForm,
                    AnswerReadingUpdateForm,
                    )


def mock_list(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    else:
        if not request.user.is_teacher:
            return redirect('student:student')
        else:    
            tests = MockTest.objects.filter(user=request.user).order_by('-time_created')
            teacher = get_object_or_404(Teacher, user=request.user)
            context = {
                'tests': tests,
                'teacher':teacher
            }
            return render (request, 'teacher/mock_list.html', context)
        

def new_mock(request):
    if request.method=='POST':
        form = NewMockForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            test = form.save(commit=False)
            test.user = request.user
            test.save()
            return redirect ('teacher:new_mock_listening', slug=test.slug)
    else:
        form = NewMockForm()
    return render (request, 'teacher/new_mock.html', {'form':form})

def new_mock_listening(request,slug):
    test = get_object_or_404(MockTest, slug=slug)
    title = test.name + ' listening'
    form = ListeningForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        listening = form.save(commit=False)
        listening.mocktest = test
        listening.save()
        return redirect ('teacher:new_mock_reading', slug=slug)

    context= {
        'form': form,
        'title': title
    }
    return render (request, 'teacher/new_mock_listening.html', context)

def new_mock_reading(request,slug):
    test = get_object_or_404(MockTest, slug=slug)
    title = test.name + ' reading'
    form = ReadingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        reading = form.save(commit=False)
        reading.mocktest = test
        reading.save()
        return redirect ('teacher:new_mock_writing', slug=slug)

    context= {
        'form': form,
        'title': title
    }
    return render (request, 'teacher/new_mock_reading.html', context)
    
def new_mock_writing(request,slug):
    test = get_object_or_404(MockTest, slug=slug)
    title = test.name + ' writing'
    form = WritingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        writing = form.save(commit=False)
        writing.mocktest = test
        writing.save()
        return redirect ('teacher:new_mock_speaking', slug=slug)

    context= {
        'form': form,
        'title': title
    }
    return render (request, 'teacher/new_mock_writing.html', context)

def new_mock_speaking(request,slug):
    test = get_object_or_404(MockTest, slug=slug)
    title = test.name + ' speaking'
    form = SpeakingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        speaking = form.save(commit=False)
        speaking.mocktest = test
        speaking.save()
        return redirect ('teacher:new_mock_al', slug=slug)

    context= {
        'form': form,
        'title': title
    }
    return render (request, 'teacher/new_mock_speaking.html', context)

def new_mock_al(request,slug):
    test = get_object_or_404(MockTest, slug=slug)
    title = test.name + ' listening answers'
    form = AnswerListeningForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        al = form.save(commit=False)
        al.mocktest = test
        al.save()
        return redirect ('teacher:new_mock_ar', slug=slug)

    context= {
        'form': form,
        'title': title
    }
    return render (request, 'teacher/new_mock_al.html', context)

def new_mock_ar(request,slug):
    test = get_object_or_404(MockTest, slug=slug)
    title = test.name + ' reading answers'
    form = AnswerReadingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        ar = form.save(commit=False)
        ar.mocktest = test
        ar.save()
        return redirect ('teacher:mock_list')

    context= {
        'form': form,
        'title': title
    }
    return render (request, 'teacher/new_mock_ar.html', context)

def mock_view(request, slug):
    mock = get_object_or_404(MockTest, slug=slug)
    instance_l = get_object_or_404(AnswerListening, mocktest=mock)
    instance_r = get_object_or_404(AnswerReading, mocktest=mock)
    if request.method ==  'GET':
        form_l = AnswerListeningUpdateForm(instance=instance_l)
        form_r = AnswerReadingUpdateForm(instance=instance_r)
    elif request.method == 'POST':
        form_l = AnswerListeningUpdateForm(request.POST or None, instance=instance_l)
        if form_l.is_valid():
            form_l.save()
        form_r = AnswerListeningUpdateForm(request.POST or None, instance=instance_r)
        if form_r.is_valid():
            form_r.save()
          

    context = {
        'mock': mock,
        'form_l': form_l,
        'form_r': form_r
    }
    return render(request, 'teacher/mock_view.html', context)