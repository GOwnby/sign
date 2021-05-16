from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Completed/<int:page>/', views.completed, name='Completed'),
    path('Sent/<int:page>/', views.sent, name='Sent'),
    path('Drafts/<int:page>/', views.drafts, name='Drafts'),
    path('Received/<int:page>/', views.received, name='Received'),
]
