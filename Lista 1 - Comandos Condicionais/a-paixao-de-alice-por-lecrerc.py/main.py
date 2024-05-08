pontuacao_charles = int(input())
pontuacao_max = int(input())
difference = abs(pontuacao_charles - pontuacao_max)

if(pontuacao_charles == 0):
    print("Oxe! E vai morrer por causa de 25 pontos?")
elif(pontuacao_charles == 25):
    print("O meu favorito venceu! Pode torar o aco Verstappen")
elif(pontuacao_charles >= 15):
    print("Esse Charles eh arretado mesmo")
elif(pontuacao_charles >= 10) and (pontuacao_charles <= 12):
    print("Ele eh desenrolado demais")

if(difference <= 4) and (pontuacao_charles != 0):
    print("Ta com a molestia, vai perder para Max Verstappen eh")
elif(difference > 4) and (pontuacao_charles > pontuacao_max):
    print("Deu o sangue")