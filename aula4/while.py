sistema = True

while sistema:
  nome = input("Your name is: ")
  print(f"O nome recebido foi: {nome}")

  if nome == "sair":
    print("Finalizou o sistema")
    break
