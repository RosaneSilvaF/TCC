import sys
import math

def calculo(numero1, numero2, numero3, numero4, numero5):
   a = numero1 + numero2 + numero3 + numero4 + numero5
   print (a)
   return numero1 + numero2 + numero3 + numero4 + numero5

def funcao_nova(valor):
    if valor > 1:
       if valor < 2:
           passou = "Sim"
       else:
           passou = "Não"
    if valor > 2:
       if valor < 3:
           passou = "Sim"
       else:
           passou = "Não"
    if valor > 3:
       if valor < 4:
           passou = "Sim"
       else:
           passou = "Não"
    if valor > 4:
       if valor < 5:
           passou = "Sim"
       else:
           passou = "Não"
    if valor > 5 :
       passou = "invalido"
    if valor < 1 :
       passou = "invalido"

    for i in lista:
        for j in lista:
            for k in lista:
                print(i, j, k)

    c = a + b
    print("Resultado: " + c)
    d = a * b
    print("Produto: " + d)
    if a > b:
       print("a é maior que b")
    if a < b:
       print("b é maior que a")
    if a == b:
       print("a e igual a b")

   # if a == b :
   #     a = a - 1
   #     print("Valor reduzido de a: " + a)

    media = (a + b) / 2
    soma = a + b
    if a > b or a == b:
        subtracao = a - b
    if b > a:
        subtracao = b - a
    if not b == 0 :
        divisao = a/b
    if b == 0 :
        divisao = "erro"
    multiplicacao = a * b

    return media, soma, subtracao, divisao, multiplicacao, passou
    return "Sim"

def funcao(lista, a, b):
    pass

def outra_funcao(a,b):
   c = a + b
   print("Resultado: " + c)
   d = a * b
   print("Produto: " + d)
   if a > b:
       print("a é maior que b")
   if a < b:
       print("b é maior que a")
   if a == b:
       print("a e igual a b")


class Numero:
   def __init__(self,valor):
       self.valor = valor


   def soma(self, numero):
       self.valor = self.valor + numero
  
   def sub(self, numero):
       self.valor = self.valor - numero
  
   def mult(self, numero):
       self.valor = self.valor * numero
  
   def div(self, numero):
       if not numero == 0:
           self.valor = self.valor / numero
       else:
           print("Erro")
  
   def valor(self):
       print(self.valor)
  
   def valor_pi(self):
       return math.pi
  
   def area_quad(self,lado1, lado2):
       area = lado1*lado2
       print(area)
       return(area)

   def printa(self, string):
       print(string)

   def printa_alfabeto(self):
       for letra in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
           print (letra)
