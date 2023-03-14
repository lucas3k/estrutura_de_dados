sair = "Sair"

while True:
  num1 = float(input("Primeiro número: "))
  num2 = float(input("Segundo número: "))
  operador = input("Informe o operador (*-+/): ")

  sair = input("Deseja sair? ").lower().startswith("s")
  if sair is True:
    break
