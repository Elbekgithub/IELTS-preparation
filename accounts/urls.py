from django.urls import path

from .views import (login_view,logout_view, student_create,profile,teacher_profile, teacher_change)


urlpatterns = [
    path('login/', login_view, name='login' ),
    path('logout/', logout_view, name='logout'),
    path('student_create/', student_create, name='student_create'),
    path('profile/', profile, name='profile'),
    path('teacher_profile/', teacher_profile, name="teacher_profile"),
    path('teacher_change/', teacher_change, name="teacher_change")
]
