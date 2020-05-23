from django.shortcuts import render,redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from .models import Teacher, Student
from .forms import UserLoginFom, TeacherForm, StudentCreationForm, ProfileForm, TeacherChangeForm


def profile(request):
    user = request.user
    if request.method =='POST':
        form = ProfileForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            if user.is_student:
                return redirect('accounts:profile')
            else:
                return redirect('accounts:teacher_profile')
    else:
        form = ProfileForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/profile.html' , context)

def teacher_change(request):
    user = request.user
    teacher = Teacher.objects.get(user=user)
    if request.method == 'POST':
        form = TeacherChangeForm(request.POST or None, instance=teacher)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect('accounts:teacher_profile')
    else:
        form = TeacherChangeForm(instance=teacher)
    return render (request, 'accounts/profile.html', {'form':form})

def teacher_profile(request):
    user = request.user
    teacher = Teacher.objects.get(user=user)
    form = ProfileForm(instance=user)
    form1 = TeacherChangeForm(instance=teacher)
    a = teacher.location
    x = a[0]
    y = a[1]
    context = {
        'teacher':teacher,
        'x':x,
        'y':y,
        'form':form,
        'form1':form1,
    }
    return render(request, 'accounts/teacher_profile.html', context)

def login_view(request):
    title = "Sign in"
    log = True
    next = request.GET.get('next')
    form = UserLoginFom(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        if next:
            return redirect(next)
        if user.is_teacher:
            return redirect("teacher:mock_list")
        if user.is_student:
            return redirect('student:student')
    return render(request, 'accounts/form.html', {'form':form, 'title': title, 'login':login})


def student_create(request):
    title = "Sign up"
    login = False
    next = request.GET.get('next')
    form = StudentCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.is_student = True
        user.save()
        Student.objects.get_or_create(user = user,)
        new_user = authenticate(username = user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("student:student") 
    context = {
        'title': title,
        'form': form,
        'login':login
    }
    return render(request, 'accounts/form.html', context)

def logout_view(request):
    logout(request)
    return redirect('main:index')