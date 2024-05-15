vote_block = ""
kanye_votes = 0
rival_votes = 0
total_votes = 0

# Primeiro Turno
while(vote_block != "FIM"):
    vote_block = input()
    if(vote_block == "FIM"):
        break
    divisible_by_2 = int(vote_block) % 2
    divisible_by_7 = int(vote_block) % 7

    if(divisible_by_7 == 0) and (divisible_by_2 != 0):
        kanye_votes += 20
        total_votes += 20
    elif(divisible_by_7 != 0) and (divisible_by_2 == 0):
        kanye_votes += 10
        total_votes += 10
    elif(divisible_by_7 != 0) and (divisible_by_2 != 0):
        rival_votes += 14
        total_votes += 14
    
    if(total_votes >= 300):
        break

if(kanye_votes > 170):
    print("O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")
    print(f"Kanye conseguiu ao final da campanha um total de {kanye_votes * 1000000} votos.")
elif(kanye_votes < 130):
    print("Caramba, não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")
    print(f"Kanye conseguiu ao final da campanha um total de {kanye_votes * 1000000} votos.")
elif(kanye_votes >= 130) and (kanye_votes <= 170):
    print("A eleição está disputada, vamos ter um segundo turno!")
    print(f"Kanye conseguiu ao final da campanha um total de {kanye_votes * 1000000} votos.")

    # Segundo Turno
    vote_block = ""
    total_votes = 0
    kanye_votes = 0
    rival_votes = 0
    while(vote_block != "FIM"):
        vote_block = input()
        if(vote_block == "FIM"):
            break
        divisible_by_2 = int(vote_block) % 2
        divisible_by_7 = int(vote_block) % 7

        if(divisible_by_7 == 0) and (divisible_by_2 != 0):
          kanye_votes += 20
          total_votes += 20
        elif(divisible_by_7 != 0) and (divisible_by_2 == 0):
          kanye_votes += 10
          total_votes += 10
        elif(divisible_by_7 != 0) and (divisible_by_2 != 0):
            rival_votes += 14
            total_votes += 14
    
        if(total_votes >= 300):
            break
    
    if(kanye_votes > 170):
        print("Depois de um pleito muito acirrado, O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")
    else:
        print("Caramba, foi uma disputa muito acirrada, mas não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")
    
    print(f"Kanye conseguiu ao final da campanha um total de {kanye_votes * 1000000} votos.")