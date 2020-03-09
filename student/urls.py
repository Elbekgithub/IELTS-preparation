from django.urls import path


from .views import mock_list, mock_view, mock_register,my_tests, test_process

urlpatterns = [
    path('', mock_list, name='student'),
    path('my-tests/', my_tests, name='my_tests'),
    path('<slug:slug>/',mock_view, name='mock_view'),
    path('<slug:slug>/test-process/',test_process, name='test_process'),
    path('<slug:slug>/mock_register/', mock_register, name='mock_register')
]
