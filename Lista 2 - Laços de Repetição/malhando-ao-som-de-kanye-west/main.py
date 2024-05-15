exercises = int(input())
tipo_treino = ""
while(tipo_treino != "Fim do Treino"):
    contagem_musicas = 0
    average = 0
    tipo_treino = input()
    if(tipo_treino != "Fim do Treino"):
        print(tipo_treino)
        for i in range(0, exercises):
            song = input()
            score = int(input())
            contagem_musicas += 1
            if(score >= 7):
                average += 1
            print(f"{contagem_musicas}° música {song} tocando agora")
            if(score >= 7):
                print("O padre Marcelo está inspirado, conseguiu finalizar suas séries!")
            elif(score < 7):
                print("O padre Marcelo está desanimado, não conseguiu finalizar suas séries")
        half = contagem_musicas / 2
        if(average >= half):
            print("ME DEI BEM COM ESSA PLAYLIST, APROVADO")
        elif(average < half):
            print("NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL")