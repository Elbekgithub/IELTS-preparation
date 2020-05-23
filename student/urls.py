from django.urls import path


from .views import (mock_list, 
                    mock_view, 
                    mock_register,
                    my_tests, 
                    test_process, 
                    answer_read, 
                    answer_list,
                    my_results,
                    answer_write,
                    answer_speak,
                    feedback,
                    certificate,
                    pdf,
                    )

urlpatterns = [
    path('', mock_list, name='student'),
    path('my-tests/', my_tests, name='my_tests'),
    path('my-results/', my_results, name='my_results'),
    path('my-results/<slug:slug>/<int:student_pk>/feedbacks/', feedback, name='feedback'),
    path('my-results/<slug:slug>/<int:student_pk>/certificate/', certificate, name='certificate'),
    path('my-results/<slug:slug>/<int:student_pk>/download/', pdf, name='download'),
    path('<slug:slug>/',mock_view, name='mock_view'),
    path('<slug:slug>/test-process/',test_process, name='test_process'),
    path('<slug:slug>/mock_register/', mock_register, name='mock_register'),
    path('<slug:slug>/answer-read/', answer_read, name='answer_read'),
    path('<slug:slug>/answer-list/', answer_list, name='answer_list'),
    path('<slug:slug>/answer-write/', answer_write, name='answer_write'),
    path('<slug:slug>/answer-speak/', answer_speak, name='answer_speak'),
]
