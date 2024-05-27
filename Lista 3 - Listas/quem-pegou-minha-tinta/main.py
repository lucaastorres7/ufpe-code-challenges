witch = ""
suspect_list = []
while(witch != "Já temos nossa lista de suspeitos"):
  witch = input()
  if(witch == "Novo suspeito - altíssima periculosidade"):
    suspect = input()
    suspect_list.insert(0, suspect)
  elif(witch == "Novo suspeito - pouco perigoso"):
    suspect = input()
    suspect_list.append(suspect)
  elif(witch == "Livre de suspeita, pode remover"):
    suspect = input()
    suspect_list.remove(suspect)
  elif(witch == "Sujeito mais perigoso do que pensávamos"):
    current_index = int(input())
    new_index = int(input())
    suspect_list[current_index], suspect_list[new_index] = suspect_list[new_index], suspect_list[current_index]
  elif(witch == "Que estranho, esses dois meliantes… troque-os de lugar"):
    suspect1 = input()
    suspect2 = input()
    index1 = suspect_list.index(suspect1)
    index2 = suspect_list.index(suspect2)
    suspect_list[index1], suspect_list[index2] = suspect_list[index2], suspect_list[index1]
  elif(witch == "Essa posição não esta de acordo, ele não e tão perigoso assim"):
    suspect = input()
    suspect_list.remove(suspect)
    suspect_list.append(suspect)
  elif(witch == "Como a lista esta ficando?"):
    for i in suspect_list:
      if(i != suspect_list[-1]):
        print(i, end=", ")
      else:
        print(i)
  elif(witch == "Já temos nossa lista de suspeitos"):
    break
print("O resultado final ficou assim:")
for i in suspect_list:
      if(i != suspect_list[-1]):
        print(i, end=", ")
      else:
        print(i)