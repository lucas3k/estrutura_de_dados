# Desenvolva um script em Python que realize o cálculo do Índice de Massa Corpórea - IMC.
# IMC = peso / altura²

peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura ** 2)
print("O IMC é", imc)
