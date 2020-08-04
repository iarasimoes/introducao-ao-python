# OPERADORES
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

print(f"OPERADORES: \n")
altura = float(input(f"Qual é a sua altura? - Ex: 1.63\n"))
altura = 72.7 * altura
altura = altura - 58 
print(f"Seu peso ideal é {int(altura)}")

# CONDICIONAIS
# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print(f"CONDICIONAIS: \n")
turno = input(f"Qual turno você estuda?\nPor favor, digite: M = Matutino | V = Vespertino | N = Noturno\n")

if turno == "M" or turno == "m":
  print("Bom Dia!") 
elif turno == "V" or turno == "v":
  print("Boa Tarde!") 
elif turno == "N" or turno == "n":
  print("Boa Noite!") 
else:
  print("Valor Inválido!")

# REPETIÇÃO
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

print(f"REPETIÇÃO: \n")
fibonacci = int(input(f"Qual número voce deseja receber a sequencia fibonacci?\n"))

count_aux1 = 0
count_aux2 = 1
count_aux3 = 1

while(count_aux3 <= fibonacci):
  print(count_aux3)
  count_aux3 = count_aux1 + count_aux2
  count_aux1 = count_aux2
  count_aux2 = count_aux3

# FUNÇÕES
# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

print(f"FUNÇÃO: \n")
def reverso_do_numero(x):
  return x[::-1]

numero = str(input(f"Qual numero voce deseja inverter?\n"))
reverso_do_numero(numero)