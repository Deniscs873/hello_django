from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade, setor):
    return HttpResponse('<h1>Hello {} de {} anos do setor {}</h1>'.format(nome, idade, setor))

def multiplicacao(request, valor1, valor2):
    return HttpResponse('<h1>Olá, você quer multiplicar o valor {} por {} e o resultado é {calc}</h1>'.format(valor1, valor2, calc= valor1 * valor2))
def adicao(request, valor1, valor2):
    return HttpResponse('<h1>Olá, você quer somar o valor {} por {} e o resultado é {calc}</h1>'.format(valor1, valor2, calc= valor1 + valor2))
def subtracao(request, valor1, valor2):
    return HttpResponse('<h1>Olá, você quer subtrair o valor {} por {} e o resultado é {calc}</h1>'.format(valor1, valor2, calc= valor1 - valor2))
def divisao(request, valor1, valor2):
    return HttpResponse('<h1>Olá, você quer dividir o valor {} por {} e o resultado é {calc}</h1>'.format(valor1, valor2, calc= valor1 / valor2))