from Funções import hello
hello()
from Funções import maior
maior(4,7)
from Funções import soma
#váriavel local 
total = 10
#chamada do módulo soma de Funções usando sua váriavel
soma(3,5)
#impressão da váriavel local do programa principal
print("Total principal = ",total)


import Funções
s = Funções.soma3(3,5)
print("Soma = ",s)
j = Funções.calcula_juros(500)
print("O juros é = ", j)

print("Resposta do Exercício 01\n")
from Ex_Funções import linha 
linha(50)
print("\nResposta do Exercício 02\n")

from Ex_Funções import imprime_lista
L = [3,6,8,9,10,9,8,4]
imprime_lista(L)

print("\n\n")
#--------------------------------------------------#


