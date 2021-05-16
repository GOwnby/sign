from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.uploaded, name='UploadDocument'),
    path('<int:requestID>/', views.ManageDocument, name='ManageDocument'),
]