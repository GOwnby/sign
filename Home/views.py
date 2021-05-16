from django.shortcuts import render

def index(request):
    return render(request, 'NewHome.html')

def Contact(request):
    return render(request, 'Contact.html')