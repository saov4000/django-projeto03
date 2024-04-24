from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})

def produtos(request):
    return render(request,'produtos.html',{})

def sobrenos(request):
    return render(request,'sobrenos.html',{})

def contato(request):
    return render(request,'contato.html',{})

