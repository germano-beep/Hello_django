from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome,idade):
    return HttpResponse('<h1>Hello {}, {} anos</h1>'.format(nome, idade))

def soma(request, num1, num2):
    resultado = num1+num2
    return HttpResponse('<h1>{}+{} = {}</h1>'.format(num1, num2, resultado))

def sub(request, num1, num2):
    resultado = num1-num2
    return HttpResponse('<h1>{}-{} = {}</h1>'.format(num1, num2, resultado))

def multplicacao(request, num1, num2):
    resultado = num1*num2
    return HttpResponse('<h1>{}*{} = {}</h1>'.format(num1, num2, resultado))

def divisao(request, num1, num2):
    resultado = num1/num2
    return HttpResponse('<h1>{}/{} = {}</h1>'.format(num1, num2, resultado))