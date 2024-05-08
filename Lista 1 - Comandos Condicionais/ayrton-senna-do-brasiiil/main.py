max_speed = int(input())
weather = input()

if(weather == "ensolarado") or (weather == "chuvoso"):
  if(max_speed >= 250) and (max_speed <= 260):
    print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")
  elif(max_speed >= 261) and (max_speed <= 285):
    print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")
  elif(max_speed >= 286) and (max_speed <= 310):
    print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")
elif(weather == "neblina"):
  if(max_speed < 250):
    print("Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!")
  elif(max_speed >= 250) and (max_speed <= 260):
    print("Senna corria em Ímola, onde infelizmente fez sua última corrida.")
  elif(max_speed >= 261) and (max_speed <= 285):
    print("Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!")