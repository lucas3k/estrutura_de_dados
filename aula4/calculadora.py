sair = "Sair"

while True:
  numValid = True

  try:
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    operador = input("Informe o operador (*-+/): ")
  except:
    numValid = False

  if not numValid:
    print("Número inválido. ")
    continue

  if operador not in ("*-+/"):
    print("Operador não aceito")

  print(eval(f"{num1} {operador} {num2}"))

  sair = input("Deseja sair? ").lower().startswith("s")
  if sair is True:
    break
