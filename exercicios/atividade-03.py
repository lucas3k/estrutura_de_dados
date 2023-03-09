# Desenvolva um script em Python que receba dois valores e exiba o maior valor recebido.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
  print("O primeiro número é maior")
elif num2 > num1:
  print("O segundo número é maior")
else:
  print("Os números são iguais")
