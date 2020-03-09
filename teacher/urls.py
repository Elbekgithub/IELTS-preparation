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
                    )               

urlpatterns = [
    path('', mock_list, name='mock_list'),
    path('add/', new_mock, name='new_mock'),
    path('add/<slug:slug>/listening/',new_mock_listening, name='new_mock_listening'),
    path('add/<slug:slug>/reading/',new_mock_reading, name='new_mock_reading'),
    path('add/<slug:slug>/writing/',new_mock_writing, name='new_mock_writing'),
    path('add/<slug:slug>/speaking/',new_mock_speaking, name='new_mock_speaking'),
    path('add/<slug:slug>/al/',new_mock_al, name='new_mock_al'),
    path('add/<slug:slug>/ar/',new_mock_ar, name='new_mock_ar'),

    path('<slug:slug>/',mock_view, name='mock_view'),
]
