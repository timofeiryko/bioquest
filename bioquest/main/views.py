from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def add(request):
    return render(request, 'add.html')

def instructions(request):
    return render(request, 'instructions.html')

def personal(request):
    return render(request, 'personal.html')

def problems(request):
    return render(request, 'problems.html')
