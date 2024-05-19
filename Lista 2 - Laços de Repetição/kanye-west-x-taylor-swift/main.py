rounds = int(input())
disorder_taylor = 0
disorder_kanye = 0
kanye_wins = 0
taylor_wins = 0
i = 0

while(i < rounds):
  kanye_points = 0
  taylor_points = 0

  print(f"{i + 1}° RODADA:")

  song_kanye = input()
  for j in range(3):
    kanye_ratings = input()
    if(kanye_ratings == "boa"):
      kanye_points += 2
    elif(kanye_ratings == "média"):
      kanye_points += 1
    elif(kanye_ratings == "ruim"):
      kanye_points -= 3
    elif(kanye_ratings == "péssima"):
      rant = ""
      while(rant != "ORDEM"):
        rant = input()
        if(rant != "ORDEM"):
          disorder_kanye += 1

  if(disorder_kanye >= 5):
    print("Os fãs do(a) Kanye West causaram tanta desordem que ele(a) perdeu o prêmio!")
    print("O(a) vencedor(a) do Cin Awards é Taylor Swift, parabéns!")
    i = rounds + 1
    continue

  else:
    song_taylor = input()
    for k in range(3):
      taylor_ratings = input()
      if(taylor_ratings == "boa"):
        taylor_points += 2
      elif(taylor_ratings == "média"):
        taylor_points += 1
      elif(taylor_ratings == "ruim"):
        taylor_points -= 3
      elif(taylor_ratings == "péssima"):
        rant = ""
        while(rant != "ORDEM"):
          rant = input()
          if(rant != "ORDEM"):
            disorder_taylor += 1
  
  if(disorder_taylor >= 5):
    print("Os fãs do(a) Taylor Swift causaram tanta desordem que ele(a) perdeu o prêmio!")
    print("O(a) vencedor(a) do Cin Awards é Kanye West, parabéns!")
    i = rounds + 1
    continue

  if(taylor_points > kanye_points):
    taylor_wins += 1
    print(f"O(a) vencedor(a) da {i + 1}° rodada foi Taylor Swift")
  elif(taylor_points < kanye_points):
    kanye_wins += 1
    print(f"O(a) vencedor(a) da {i + 1}° rodada foi Kanye West")
  else:
    print(f"Não houve vencedor na {i + 1}° rodada")
  if(kanye_wins == 3):
    print(f"O(a) vencedor(a) do Cin Awards, com um total de {kanye_wins} vitórias, é Kanye West, parabéns!")
    i = rounds + 1
    continue
  elif(taylor_wins == 3):
    print(f"O(a) vencedor(a) do Cin Awards, com um total de {taylor_wins} vitórias, é Taylor Swift, parabéns!")
    i = rounds + 1
    continue
  i += 1

if(disorder_taylor < 5) and (disorder_kanye < 5) and (kanye_wins < 3) and (taylor_wins < 3):
  if(taylor_wins > kanye_wins):
    print(f"O(a) vencedor(a) do Cin Awards, com um total de {taylor_wins} vitórias, é Taylor Swift, parabéns!")
  elif(taylor_wins < kanye_wins):
    print(f"O(a) vencedor(a) do Cin Awards, com um total de {kanye_wins} vitórias, é Kanye West, parabéns!")
  else:
    print("Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!")