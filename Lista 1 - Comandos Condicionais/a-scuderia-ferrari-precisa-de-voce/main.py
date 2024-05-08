laps = int(input())
weather = input()
difficulty = input()
tire = input()
durability = 0

if(tire == "chuva") and (weather == "sol"):
    durability = 50
    durability -= laps * 15
elif(tire != "chuva") and (weather == "chuva"):
    if(tire == "macio"):
        durability = 50
        durability -= laps * 15
    elif(tire == "médio"):
        durability = 70
        durability -= laps * 15
    elif(tire == "duro"):
        durability = 90
        durability -= laps * 15
elif(weather == "sol") and (difficulty != "alta") and (tire == "macio" or "médio"):
    if(tire == "macio"):
        durability = 50
        durability -= laps * 2
    elif(tire == "médio"):
        durability = 70
        durability -= laps * 2
elif(weather == "sol") and (difficulty == "alta") and (tire == "macio"):
    durability = 50
    durability -= laps * 3
elif(weather == "sol") and (difficulty == "alta") and (tire == "duro"):
    durability = 90
    durability -= laps
elif(weather == "chuva") and (tire == "chuva"):
    if(difficulty == "baixa"):
        durability = 50
        durability -= laps
    elif(difficulty == "média"):
        durability = 50
        durability -= laps * 2
    elif(difficulty == "alta"):
        durability = 50
        durability -= laps * 3

if(durability >= 20):
    print(f"A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {durability}.")
elif(durability < 20):
    print(f"Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {durability} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.")