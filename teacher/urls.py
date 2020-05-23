from django.urls import path


from .views import (mock_list, 
                    new_mock, 
                    new_mock_listening, 
                    new_mock_reading, 
                    new_mock_speaking, 
                    new_mock_writing, 
                    new_mock_al, 
                    new_mock_ar,
                    mock_view,
                    student_results,
                    student_results_check1,
                    student_results_check2
                    )               

urlpatterns = [
    path('', mock_list, name='mock_list'),
    path('add/', new_mock, name='new_mock'),
    path('student-answers/', student_results, name='student_results'),
    path('student-answers/<slug:slug>/<int:student_pk>/writing', student_results_check1, name='student_results_check1'),
    path('student-answers/<slug:slug>/<int:student_pk>/speaking', student_results_check2, name='student_results_check2'),
    path('add/<slug:slug>/listening/',new_mock_listening, name='new_mock_listening'),
    path('add/<slug:slug>/reading/',new_mock_reading, name='new_mock_reading'),
    path('add/<slug:slug>/writing/',new_mock_writing, name='new_mock_writing'),
    path('add/<slug:slug>/speaking/',new_mock_speaking, name='new_mock_speaking'),
    path('add/<slug:slug>/al/',new_mock_al, name='new_mock_al'),
    path('add/<slug:slug>/ar/',new_mock_ar, name='new_mock_ar'),

    path('<slug:slug>/',mock_view, name='mock_view'),
]
