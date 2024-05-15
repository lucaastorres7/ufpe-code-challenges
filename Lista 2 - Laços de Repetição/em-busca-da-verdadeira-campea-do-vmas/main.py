students = int(input())
taylor_votes = 0
beyonce_votes = 0

for i in range(students):
  vote = input()
  if(vote == "beyonce"):
    print(f"Aluno {i+1} votou na Beyoncé.")
    beyonce_votes += 1
  elif(vote == "taylor swift"):
    print(f"Aluno {i+1} votou na Taylor Swift.")
    taylor_votes += 1

print("Contagem de votos:")
print(f"Taylor Swift: {taylor_votes} votos")
print(f"Beyoncé: {beyonce_votes} votos")

if(taylor_votes == beyonce_votes):
  print("Empate! Iniciando rodada de debate.")
  print("Alunos, agora é a sua chance de convencer os outros a mudar de voto!")
  for j in range(students):
    change_vote = input()
    if(change_vote == "sim"):
      new_vote = input()
      if(new_vote == "taylor swift"):
        print(f"Aluno {j+1} mudou seu voto para Taylor Swift.")
        taylor_votes += 1
      if(new_vote == "beyonce"):
        print(f"Aluno {j+1} mudou seu voto para Beyoncé.")
        beyonce_votes += 1
    elif(change_vote == "nao"):
      print(f"Aluno {j+1} não mudou seu voto.")
  
  print("Nova contagem de votos após o debate:")
  print(f"Taylor Swift: {taylor_votes} votos")
  print(f"Beyoncé: {beyonce_votes} votos")

if(taylor_votes > beyonce_votes):
  print(f"Taylor Swift venceu com {taylor_votes} votos! Kanye West tá irritado com isso.")
elif(taylor_votes < beyonce_votes):
  print(f"Beyoncé venceu com {beyonce_votes} votos! Será que Kanye West estava certo?")
else:
  print("Aldo, como presidente do evento, tem o voto decisivo.")
  decisive_vote = input()

  if(decisive_vote == "taylor swift"):
    print("Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso.")
  elif(decisive_vote == "beyonce"):
    print("Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?")