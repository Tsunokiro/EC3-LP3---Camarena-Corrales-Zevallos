from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def saludo(request):
    return render(request, 'saludo.html')