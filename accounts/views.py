from django.shortcuts import render,redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from .models import Teacher, Student
from .forms import UserLoginFom, TeacherCreationForm, StudentCreationForm

def login_view(request):
    title = "Login"
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
            return redirect("teacher")
        if user.is_student:
            return redirect('student')
    return render(request, 'accounts/form.html', {'form':form, 'title': title})


def student_create(request):
    title = "Student Signup"
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
        return redirect("/") 
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')