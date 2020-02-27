from django.urls import path

from .views import (login_view,logout_view, student_create)


urlpatterns = [
    path('login/', login_view, name='login' ),
    path('logout/', logout_view, name='logut'),
    path('student_create/', student_create, name='student_create'),
]
