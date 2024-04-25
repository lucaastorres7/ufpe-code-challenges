lewis = "Lewis Hamilton"
maxv = "Max Verstappen"
valtteri = "Valtteri Bottas"
lewis_total_points = int(input())
lewis_last_race = int(input())
max_total_points = int(input())
max_last_race = int(input())
valtteri_total_points = int(input())
valtteri_last_race = int(input())

if (lewis_last_race <= 10):
    lewis_total_points += 5
if (max_last_race <= 10):
    max_total_points += 5
if (valtteri_last_race <= 10):
    valtteri_total_points += 5

if(lewis_total_points > max_total_points) and (lewis_total_points > valtteri_total_points):
    print(f"{lewis} ganhou a competição com {lewis_total_points} pontos!")
elif(max_total_points > lewis_total_points) and (max_total_points > valtteri_total_points):
    print(f"{maxv} ganhou a competição com {max_total_points} pontos!")
elif(valtteri_total_points > max_total_points) and (valtteri_total_points > lewis_total_points):
    print(f"{valtteri} ganhou a competição com {valtteri_total_points} pontos!")
elif(lewis_total_points == max_total_points) and (lewis_total_points == valtteri_total_points):
    print(f"{lewis} ganhou a competição com {lewis_total_points} pontos!")
elif(valtteri_total_points == max_total_points):
    print(f"{maxv} ganhou a competição com {max_total_points} pontos!")
elif(valtteri_total_points == lewis_total_points):
    print(f"{lewis} ganhou a competição com {lewis_total_points} pontos!")
elif(lewis_total_points == max_total_points):
    print(f"{lewis} ganhou a competição com {lewis_total_points} pontos!")