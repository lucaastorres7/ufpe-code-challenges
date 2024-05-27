animal_quantity = int(input())
catalog = []
i = 0

while len(catalog) < animal_quantity:
  command = input()
  if(command == "REGISTRA"):
    animal = input()
    if(animal in catalog):
      print(f"{animal} já foi registrado antes!")
    else:
      catalog.append(animal)
      print(f"{animal} registrado com sucesso.")
  elif(command == "CORRIGE"):
    if(len(catalog) > 0):
      print("Último registro apagado com sucesso.")
      catalog.remove(animal)
    else:
      print("O catálogo ainda está vazio.")
  elif(command == "REINICIA"):
    catalog = []
    print("Catálogo redefinido com sucesso.")
    
print("Todos os animais foram registrados!")
print("")
print("Catálogo de animais:")

for name in catalog:
  i += 1
  print(f"{i}º: {name}")