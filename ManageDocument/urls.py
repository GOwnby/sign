from django.urls import path

import views

urlpatterns = [
    path('upload/', views.uploaded, name='UploadDocument')
    path('<int:requestID>/', views.ManageDocument, name='ManageDocument')
]