from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request,'home.html',{})

def produtos(request):
    produtos = Produto.objects.all()
    return render(request,'produtos.html',{"produtos":produtos})

def sobrenos(request):
    return render(request,'sobrenos.html',{})

def contato(request):
    return render(request,'contato.html',{})

