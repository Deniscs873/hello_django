from django.shortcuts import render , HttpResponse

# Create your views here.

def hello(request, nome, idade, setor):
    return HttpResponse('<h1>Hello {} de {} anos do setor {}</h1>'.format(nome, idade, setor))