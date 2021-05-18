from django.urls import path

from . import views

urlpatterns = [
    path('Upload/', views.uploaded, name='UploadDocument'),
    path('<str:requestID>/', views.ManageDocument, name='ManageDocument'),
    path('Editor/<str:requestID>/', views.PdfEditor, name='EditDocument'),
]