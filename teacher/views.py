from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from datetime import datetime
from django.contrib.auth import get_user_model

from .models import MockTest, Listening, Reading, Writing, Speaking, AnswerListening, AnswerReading, AnswerListeningChecked, AnswerReadingChecked
from accounts.models import Teacher
from student.models import AnswerReadingStudent, AnswerListeningStudent,AnswerSpeakingStudent, AnswerWritingStudent
from .forms import (NewMockForm, 
                    ListeningForm, 
                    ReadingForm, 
                    WritingForm, 
                    SpeakingForm, 
                    AnswerListeningForm, 
                    AnswerReadingForm, 
                    AnswerListeningUpdateForm,
                    AnswerReadingUpdateForm,
                    AnswerWritingCheckForm,
                    AnswerSpeakingCheckForm,
                    )

User = get_user_model()

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
                'teacher':teacher,
                
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


def student_results(request):
    now = datetime.now()
    write_results = AnswerWritingStudent.objects.filter(create_time__day__lte = now.day).filter(mocktest__user = request.user)
    speak_results = AnswerSpeakingStudent.objects.filter(create_time__day__lte = now.day).filter(mocktest__user = request.user)
    context = {
        'write_results':write_results,
        'speak_results':speak_results
    }
    return render(request, 'teacher/student_results.html', context)

def student_results_check1(request, slug,student_pk):
    mock = MockTest.objects.get(slug=slug)
    answer_writing = AnswerWritingStudent.objects.filter(mocktest=mock).filter(student__pk = student_pk).first()
    answer = AnswerListeningStudent.objects.filter(mocktest=mock).filter(student__pk = student_pk).first()
    answerlistening = AnswerListening.objects.get(mocktest=mock)
    correct = int(0)
    if request.method=='POST':
        form = AnswerWritingCheckForm(request.POST or None)
        if form.is_valid():
            test = form.save(commit=False)
            test.mocktest = mock
            test.student = User.objects.get(pk=student_pk)
            test.save()
            answer_writing.is_checked = True
            answer_writing.save()
            if  answerlistening.a1 == answer.a1:
                correct+=1
            if answerlistening.a2 == answer.a2:
                correct+=1
            if answerlistening.a3 == answer.a3:
                correct+=1
            if answerlistening.a4 == answer.a4:
                correct+=1
            if answerlistening.a5 == answer.a5:
                correct+=1
            if answerlistening.a6 == answer.a6:
                correct+=1
            if answerlistening.a7 == answer.a7:
                correct+=1
            if answerlistening.a8 == answer.a8:
                correct+=1
            if answerlistening.a9 == answer.a9:
                correct+=1
            if answerlistening.a10 == answer.a10:
                correct+=1
            if answerlistening.a11 == answer.a11:
                correct+=1
            if answerlistening.a12 == answer.a12:
                correct+=1
            if answerlistening.a13 == answer.a13:
                correct+=1
            if answerlistening.a14 == answer.a14:
                correct+=1
            if answerlistening.a15 == answer.a15:
                correct+=1
            if answerlistening.a16 == answer.a16:
                correct+=1
            if answerlistening.a17 == answer.a17:
                correct+=1
            if answerlistening.a18 == answer.a18:
                correct+=1
            if answerlistening.a19 == answer.a19:
                correct+=1
            if answerlistening.a20 == answer.a20:
                correct+=1
            if answerlistening.a21 == answer.a21:
                correct+=1
            if answerlistening.a22 == answer.a22:
                correct+=1
            if answerlistening.a23 == answer.a23:
                correct+=1
            if answerlistening.a24 == answer.a24:
                correct+=1
            if answerlistening.a25 == answer.a25:
                correct+=1
            if answerlistening.a26 == answer.a26:
                correct+=1
            if answerlistening.a27 == answer.a27:
                correct+=1
            if answerlistening.a28 == answer.a28:
                correct+=1
            if answerlistening.a29 == answer.a29:
                correct+=1
            if answerlistening.a30 == answer.a30:
                correct+=1
            if answerlistening.a31 == answer.a31:
                correct+=1
            if answerlistening.a32 == answer.a32:
                correct+=1
            if answerlistening.a33 == answer.a33:
                correct+=1
            if answerlistening.a34 == answer.a34:
                correct+=1
            if answerlistening.a35 == answer.a35:
                correct+=1
            if answerlistening.a36 == answer.a36:
                correct+=1
            if answerlistening.a37 == answer.a37:
                correct+=1
            if answerlistening.a38 == answer.a38:
                correct+=1 
            if answerlistening.a39 == answer.a39:
                correct+=1   
            if answerlistening.a40 == answer.a40:
                correct+=1
            if correct < 15:
                band=4
            elif correct >=15 and correct <17:
                band=5
            elif correct >=17 and correct <22:
                band=5.5
            elif correct >=22 and correct <26:
                band=6
            elif correct >=26 and correct <30:
                band=6.5
            elif correct >=30 and correct <33:
                band=7
            elif correct >=33 and correct <35:
                band=7.5
            elif correct >=35 and correct <37:
                band=8
            elif correct >=37 and correct <39:
                band=8.5
            elif correct >=39 and correct <=40:
                band=9
            AnswerListeningChecked.objects.get_or_create(
                mocktest=mock,
                student=User.objects.get(pk=student_pk),
                band=correct,
            )
            return redirect ('teacher:student_results_check2', slug=slug, student_pk=student_pk)
    else:
        form = AnswerWritingCheckForm()
    context = {
        'mocktest':mock,
        'answer_writing':answer_writing,
        'form':form,
        'answer':answer,
        'answerlistening':answerlistening,
    }
    return render(request, 'teacher/student_results_check1.html', context)

def student_results_check2(request, slug,student_pk):
    mock = MockTest.objects.get(slug=slug)
    answer_speaking = AnswerSpeakingStudent.objects.filter(mocktest=mock).filter(student__pk = student_pk).first()
    answer = AnswerReadingStudent.objects.filter(mocktest=mock).filter(student__pk = student_pk).first()
    correct = int(0)
    if request.method=='POST':
        form = AnswerSpeakingCheckForm(request.POST or None)
        if form.is_valid():
            test = form.save(commit=False)
            test.mocktest = mock
            test.student = User.objects.get(pk=student_pk)
            test.save()
            answer_speaking.is_checked = True
            answer_speaking.save()

            if mock.answerreading.a1 == answer.a1:
                correct+=1
            if mock.answerreading.a2 == answer.a2:
                correct+=1
            if mock.answerreading.a3 == answer.a3:
                correct+=1
            if mock.answerreading.a4 == answer.a4:
                correct+=1
            if mock.answerreading.a5 == answer.a5:
                correct+=1
            if mock.answerreading.a6 == answer.a6:
                correct+=1
            if mock.answerreading.a7 == answer.a7:
                correct+=1
            if mock.answerreading.a8 == answer.a8:
                correct+=1
            if mock.answerreading.a9 == answer.a9:
                correct+=1
            if mock.answerreading.a10 == answer.a10:
                correct+=1
            if mock.answerreading.a11 == answer.a11:
                correct+=1
            if mock.answerreading.a12 == answer.a12:
                correct+=1
            if mock.answerreading.a13 == answer.a13:
                correct+=1
            if mock.answerreading.a14 == answer.a14:
                correct+=1
            if mock.answerreading.a15 == answer.a15:
                correct+=1
            if mock.answerreading.a16 == answer.a16:
                correct+=1
            if mock.answerreading.a17 == answer.a17:
                correct+=1
            if mock.answerreading.a18 == answer.a18:
                correct+=1
            if mock.answerreading.a19 == answer.a19:
                correct+=1
            if mock.answerreading.a20 == answer.a20:
                correct+=1
            if mock.answerreading.a21 == answer.a21:
                correct+=1
            if mock.answerreading.a22 == answer.a22:
                correct+=1
            if mock.answerreading.a23 == answer.a23:
                correct+=1
            if mock.answerreading.a24 == answer.a24:
                correct+=1
            if mock.answerreading.a25 == answer.a25:
                correct+=1
            if mock.answerreading.a26 == answer.a26:
                correct+=1
            if mock.answerreading.a27 == answer.a27:
                correct+=1
            if mock.answerreading.a28 == answer.a28:
                correct+=1
            if mock.answerreading.a29 == answer.a29:
                correct+=1
            if mock.answerreading.a30 == answer.a30:
                correct+=1
            if mock.answerreading.a31 == answer.a31:
                correct+=1
            if mock.answerreading.a32 == answer.a32:
                correct+=1
            if mock.answerreading.a33 == answer.a33:
                correct+=1
            if mock.answerreading.a34 == answer.a34:
                correct+=1
            if mock.answerreading.a35 == answer.a35:
                correct+=1
            if mock.answerreading.a36 == answer.a36:
                correct+=1
            if mock.answerreading.a37 == answer.a37:
                correct+=1
            if mock.answerreading.a38 == answer.a38:
                correct+=1 
            if mock.answerreading.a39 == answer.a39:
                correct+=1   
            if mock.answerreading.a40 == answer.a40:
                correct+=1
            if correct < 15:
                band=4
            elif correct >=15 and correct <17:
                band=5
            elif correct >=17 and correct <22:
                band=5.5
            elif correct >=22 and correct <26:
                band=6
            elif correct >=26 and correct <30:
                band=6.5
            elif correct >=30 and correct <33:
                band=7
            elif correct >=33 and correct <35:
                band=7.5
            elif correct >=35 and correct <37:
                band=8
            elif correct >=37 and correct <39:
                band=8.5
            elif correct >=39 and correct <=40:
                band=9
            AnswerReadingChecked.objects.get_or_create(
                mocktest=mock,
                student=User.objects.get(pk=student_pk),
                band=band,
                correct=correct,
            )
            return redirect ('teacher:student_results')
    else:
        form = AnswerSpeakingCheckForm()
    context = {
        'mocktest':mock,
        'form':form,
        'answer_speaking':answer_speaking,
        'answer':answer,
        'answerreading':mock.answerreading,
    }
    return render(request, 'teacher/student_results_check2.html', context)