from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import get_user_model
from .utils import Render
User = get_user_model()
# Create your views here.
from .forms import AnswerWritingForm, MockRegisterForm
from .models import AnswerReadingStudent, AnswerListeningStudent, AnswerSpeakingStudent, AnswerWritingStudent
from teacher.models import MockTest, AnswerListening, AnswerReading,AnswerListeningChecked,AnswerReadingChecked,AnswerSpeakingChecked,AnswerWritingChecked
from accounts.models import Teacher


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
    user = User.objects.get(id=mock.user.id)
    teacher = Teacher.objects.get(user=user)
    a = teacher.location
    x = a[0]
    y = a[1]
    context = {
        'mock': mock,
        'x':x,
        'y':y,
        'teacher':teacher,
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
    answer = mock.answerspeakingstudent_set.filter(student=request.user).first()
    context = {
        'mock':mock,
        'answer':answer
    }
    return render(request, 'student/test_process.html', context)


def answer_read(request,slug):
    mock = get_object_or_404(MockTest, slug=slug)
    if AnswerReadingStudent.objects.filter(mocktest=mock).filter(student=request.user).exists():
        answer = mock.answerreadingstudent_set.filter(student=request.user).first()
        if request.method == 'POST':
            answer.a1 = request.POST['a1']
            answer.a2 = request.POST['a2']
            answer.a3 = request.POST['a3']
            answer.a4 = request.POST['a4']
            answer.a5 = request.POST['a5']
            answer.a6 = request.POST['a6']
            answer.a7 = request.POST['a7']
            answer.a8 = request.POST['a8']
            answer.a9 = request.POST['a9']
            answer.a10 = request.POST['a10']
            answer.a11 = request.POST['a11']
            answer.a12 = request.POST['a12']
            answer.a13 = request.POST['a13']
            answer.a14 = request.POST['a14']
            answer.a15 = request.POST['a15']
            answer.a16 = request.POST['a16']
            answer.a17 = request.POST['a17']
            answer.a18 = request.POST['a18']
            answer.a19 = request.POST['a19']
            answer.a20 = request.POST['a20']
            answer.a21 = request.POST['a21']
            answer.a22 = request.POST['a22']
            answer.a23 = request.POST['a23']
            answer.a24 = request.POST['a24']
            answer.a25 = request.POST['a25']
            answer.a26 = request.POST['a26']
            answer.a27 = request.POST['a27']
            answer.a28 = request.POST['a28']
            answer.a29 = request.POST['a29']
            answer.a30 = request.POST['a30']
            answer.a31 = request.POST['a31']
            answer.a32 = request.POST['a32']
            answer.a33 = request.POST['a33']
            answer.a34 = request.POST['a34']
            answer.a35 = request.POST['a35']
            answer.a36 = request.POST['a36']
            answer.a38 = request.POST['a38']
            answer.a39 = request.POST['a39']
            answer.a40 = request.POST['a40']
            answer.save()
    else:
        if request.method == 'POST':
            AnswerReadingStudent.objects.create(
                mocktest = mock,
                student = request.user,
                a1 = request.POST.get('a1'),
                a2 = request.POST.get('a2'),
                a3 = request.POST.get('a3'),
                a4 = request.POST.get('a4'),
                a5 = request.POST.get('a5'),
                a6 = request.POST.get('a6'),
                a7 = request.POST.get('a7'),
                a8 = request.POST.get('a8'),
                a9 = request.POST.get('a9'),
                a10 = request.POST.get('a10'),
                a11 = request.POST.get('a11'),
                a12 = request.POST.get('a12'),
                a13 = request.POST.get('a13'),
                a14 = request.POST.get('a14'),
                a15 = request.POST.get('a15'),
                a16 = request.POST.get('a16'),
                a17 = request.POST.get('a17'),
                a18 = request.POST.get('a18'),
                a19 = request.POST.get('a19'),
                a20 = request.POST.get('a20'),
                a21 = request.POST.get('a21'),
                a22 = request.POST.get('a22'),
                a23 = request.POST.get('a23'),
                a24 = request.POST.get('a24'),
                a25 = request.POST.get('a25'),
                a26 = request.POST.get('a26'),
                a27 = request.POST.get('a27'),
                a28 = request.POST.get('a28'),
                a29 = request.POST.get('a29'),
                a30 = request.POST.get('a30'),
                a31 = request.POST.get('a31'),
                a32 = request.POST.get('a32'),
                a33 = request.POST.get('a33'),
                a34 = request.POST.get('a34'),
                a35 = request.POST.get('a35'),
                a36 = request.POST.get('a36'),
                a37 = request.POST.get('a37'),
                a38 = request.POST.get('a38'),
                a39 = request.POST.get('a39'),
                a40 = request.POST.get('a40'),
            )

    return redirect('student:test_process', slug=slug)

def answer_list(request,slug):
    mock = get_object_or_404(MockTest, slug=slug)
    if AnswerListeningStudent.objects.filter(mocktest=mock).filter(student=request.user).exists():
        answer = mock.answerlisteningstudent_set.filter(student=request.user).first()
        if request.method == 'POST':
            answer.a1 = request.POST['a1']
            answer.a2 = request.POST['a2']
            answer.a3 = request.POST['a3']
            answer.a4 = request.POST['a4']
            answer.a5 = request.POST['a5']
            answer.a6 = request.POST['a6']
            answer.a7 = request.POST['a7']
            answer.a8 = request.POST['a8']
            answer.a9 = request.POST['a9']
            answer.a10 = request.POST['a10']
            answer.a11 = request.POST['a11']
            answer.a12 = request.POST['a12']
            answer.a13 = request.POST['a13']
            answer.a14 = request.POST['a14']
            answer.a15 = request.POST['a15']
            answer.a16 = request.POST['a16']
            answer.a17 = request.POST['a17']
            answer.a18 = request.POST['a18']
            answer.a19 = request.POST['a19']
            answer.a20 = request.POST['a20']
            answer.a21 = request.POST['a21']
            answer.a22 = request.POST['a22']
            answer.a23 = request.POST['a23']
            answer.a24 = request.POST['a24']
            answer.a25 = request.POST['a25']
            answer.a26 = request.POST['a26']
            answer.a27 = request.POST['a27']
            answer.a28 = request.POST['a28']
            answer.a29 = request.POST['a29']
            answer.a30 = request.POST['a30']
            answer.a31 = request.POST['a31']
            answer.a32 = request.POST['a32']
            answer.a33 = request.POST['a33']
            answer.a34 = request.POST['a34']
            answer.a35 = request.POST['a35']
            answer.a36 = request.POST['a36']
            answer.a38 = request.POST['a38']
            answer.a39 = request.POST['a39']
            answer.a40 = request.POST['a40']
            answer.save()
    else:
        if request.method == 'POST':
            AnswerListeningStudent.objects.create(
                mocktest = mock,
                student = request.user,
                a1 = request.POST.get('a1'),
                a2 = request.POST.get('a2'),
                a3 = request.POST.get('a3'),
                a4 = request.POST.get('a4'),
                a5 = request.POST.get('a5'),
                a6 = request.POST.get('a6'),
                a7 = request.POST.get('a7'),
                a8 = request.POST.get('a8'),
                a9 = request.POST.get('a9'),
                a10 = request.POST.get('a10'),
                a11 = request.POST.get('a11'),
                a12 = request.POST.get('a12'),
                a13 = request.POST.get('a13'),
                a14 = request.POST.get('a14'),
                a15 = request.POST.get('a15'),
                a16 = request.POST.get('a16'),
                a17 = request.POST.get('a17'),
                a18 = request.POST.get('a18'),
                a19 = request.POST.get('a19'),
                a20 = request.POST.get('a20'),
                a21 = request.POST.get('a21'),
                a22 = request.POST.get('a22'),
                a23 = request.POST.get('a23'),
                a24 = request.POST.get('a24'),
                a25 = request.POST.get('a25'),
                a26 = request.POST.get('a26'),
                a27 = request.POST.get('a27'),
                a28 = request.POST.get('a28'),
                a29 = request.POST.get('a29'),
                a30 = request.POST.get('a30'),
                a31 = request.POST.get('a31'),
                a32 = request.POST.get('a32'),
                a33 = request.POST.get('a33'),
                a34 = request.POST.get('a34'),
                a35 = request.POST.get('a35'),
                a36 = request.POST.get('a36'),
                a37 = request.POST.get('a37'),
                a38 = request.POST.get('a38'),
                a39 = request.POST.get('a39'),
                a40 = request.POST.get('a40'),
                
            )
    return redirect('student:test_process', slug=slug)



def answer_write(request,slug):
    mock = get_object_or_404(MockTest, slug=slug)
    if AnswerWritingStudent.objects.filter(mocktest=mock).filter(student=request.user).exists():
        answer = mock.answerwritingstudent_set.filter(student=request.user).first()
        if request.method == 'POST' and request.FILES['pdf']:
            answer.task1 = request.POST['task1']
            answer.task2 = request.POST['task2']
            answer.pdf = request.FILES['pdf']
            answer.save()
    else:
        if request.method == 'POST' and request.FILES['pdf']:
            AnswerWritingStudent.objects.create(
                mocktest = mock,
                student = request.user,
                task1 = request.POST.get('task1'),
                task2 = request.POST.get('task2'),
                pdf = request.FILES['pdf']
            )
    return redirect('student:test_process', slug=slug)

def answer_speak(request,slug):
    mock = get_object_or_404(MockTest, slug=slug)
    if AnswerSpeakingStudent.objects.filter(mocktest=mock).filter(student=request.user).exists():
        answer = mock.answerspeakingstudent_set.filter(student=request.user).first()
        if request.method == 'POST' and request.FILES['audio']:
            answer.audio = request.FILES['audio']
            answer.save()
    else:
        if request.method == 'POST' and request.FILES['audio']:
            AnswerSpeakingStudent.objects.create(
                mocktest = mock,
                student = request.user,
                audio = request.FILES['audio']
            )
    return redirect('student:test_process', slug=slug)
        



def my_results(request):
    write_results = AnswerWritingStudent.objects.filter(student = request.user).filter(is_checked = True)
    context = {
        'write_results':write_results,
    }
    return render(request, 'student/my_results.html', context)


def feedback(request, slug, student_pk):
    mocktest = MockTest.objects.get(slug=slug)
    listening = AnswerListeningChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    reading = AnswerReadingChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    writing = AnswerWritingChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    speaking = AnswerSpeakingChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    context = {
        'listening':listening,
        'reading':reading,
        'writing':writing,
        'speaking':speaking,
    }
    return render(request, 'student/feedback.html', context)

def certificate(request, slug, student_pk):
    mocktest = MockTest.objects.get(slug=slug)
    answer_write = AnswerWritingStudent.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    listening = AnswerListeningChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    reading = AnswerReadingChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    writing = AnswerWritingChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    speaking = AnswerSpeakingChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    overall = (listening.band + reading.band + writing.band + speaking.band)/4
    kasr = overall-int(overall)
    if kasr >= 0 and kasr < 0.25:
        kasr = 0
    elif kasr >= 0.25 and kasr < 0.75:
        kasr = 0.5
    elif kasr >= 0.75 and kasr < 1:
        kasr = 1
    overall = int(overall) + kasr
    context = {
        'listening':listening,
        'reading':reading,
        'writing':writing,
        'speaking':speaking,
        'overall':overall,
        'answer_write':answer_write,

    }
    return render(request, 'student/certificate.html', context)




def pdf(request, slug, student_pk):
    mocktest = MockTest.objects.get(slug=slug)
    answer_write = AnswerWritingStudent.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    listening = AnswerListeningChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    reading = AnswerReadingChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    writing = AnswerWritingChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    speaking = AnswerSpeakingChecked.objects.filter(mocktest=mocktest).filter(student_id=student_pk).first()
    overall = (listening.band + reading.band + writing.band + speaking.band)/4
    kasr = overall-int(overall)
    if kasr >= 0 and kasr < 0.25:
        kasr = 0
    elif kasr >= 0.25 and kasr < 0.75:
        kasr = 0.5
    elif kasr >= 0.75 and kasr < 1:
        kasr = 1
    overall = int(overall) + kasr
    params = {
        'listening':listening,
        'reading':reading,
        'writing':writing,
        'speaking':speaking,
        'overall':overall,
        'answer_write':answer_write,
    }
    return Render.render('student/pdf.html', params)