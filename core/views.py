from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,nome,idade):
    return HttpResponse('<h1>Hello World {} de {} anos ! </h1>'.format(nome,idade))


def soma(request,numero1,numero2):
    resultado = numero1 + numero2
    return HttpResponse ('A Soma de {} + {} é igual a = {}'.format(numero1,numero2,resultado))

def subtracao(request,numero1,numero2):
    resultado = numero1 - numero2
    return HttpResponse ('A subtracao de {} - {} é igual a = {}'.format(numero1,numero2,resultado))

def divisao(request,numero1,numero2):
    resultado = numero1 / numero2
    return HttpResponse ('A Divisão de {} / {} é igual a = {}'.format(numero1,numero2,resultado))

def multiplicacao(request,numero1,numero2):
    resultado = numero1 * numero2
    return HttpResponse ('A Multiplicação de {} x {} é igual a = {}'.format(numero1,numero2,resultado))
