candidate1 = input()
candidate2 = input()
state_electors = ""
electors1 = 0
electors2 = 0
total_votes1 = 0
total_votes2 = 0

if(candidate1 != "Kanye West") and (candidate2 != "Kanye West"):
    print("Sem o Ye, sem eleição!")

else:
    while(state_electors != "FIM"):
        state_electors = input()
        if(state_electors == "FIM"):
            break
        state, electors = state_electors.split(", ")
        votes1 = input() # Candidato 1

        while(votes1 == "Taylor Swift roubou as urnas!"):
            votes1 = ""
            votes2 = ""
            print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
            votes1 = input() # Candidato 1

        votes2 = input() # Candidato 2

        while(votes2 == "Taylor Swift roubou as urnas!"):
            votes1 = ""
            votes2 = ""
            print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
            votes1 = input() # Candidato 1
            while(votes1 == "Taylor Swift roubou as urnas!"):
                votes1 = ""
                votes2 = ""
                print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
                votes1 = input() # Candidato 1
            votes2 = input() # Candidato 2
        

        total = int(votes1) + int(votes2)
        votes_porcentage1 = (int(votes1) / total) * 100
        votes_porcentage2 = (int(votes2) / total) * 100

        if(int(votes1) > int(votes2)):
            print(f"{candidate1} obteve maioria no(a) {state} com {int(votes_porcentage1)}% dos votos.")
            electors1 += int(electors)
            total_votes1 += int(votes1)
        elif(int(votes1) < int(votes2)):
            print(f"{candidate2} obteve maioria no(a) {state} com {int(votes_porcentage2)}% dos votos.")
            electors2 += int(electors)
            total_votes2 += int(votes2)

    if(electors1 > electors2):
        print(f"Temos o resultado final! {candidate1} vence a disputa pela presidência, com o apoio de {electors1} delegados do colégio eleitoral e {total_votes1} votos populares.")
        if(candidate1 == "Kanye West"):
            print("\"Everybody wanted to know what I would do if I didn't win... I Guess We'll Never Know.\"")
        else:
            print("\"Não tem problema, eu obtive o molho!\"")
    elif(electors1 < electors2):
        print(f"Temos o resultado final! {candidate2} vence a disputa pela presidência, com o apoio de {electors2} delegados do colégio eleitoral e {total_votes2} votos populares.")
        if(candidate2 == "Kanye West"):
            print("\"Everybody wanted to know what I would do if I didn't win... I Guess We'll Never Know.\"")
        else:
            print("\"Não tem problema, eu obtive o molho!\"")