constructor1 = input()
position1 = int(input())
salary_in_millions_1 = int(input())
constructor2 = input()
position2 = int(input())
salary_in_millions_2 = int(input())
score1, score2 = 0, 0

if (constructor1 == "Red Bull"):
    score1 += 3
    if (position1 == 1):
        score1 += 3
        score1 += salary_in_millions_1 / 4
    elif (position1 == 2):
        score1 += 2
        score1 += salary_in_millions_1 / 4
    elif (position1 == 3):
        score1 = score1
elif (constructor1 == "McLaren"):
    score1 += 2
    if (position1 == 1):
        score1 += 3
        score1 += salary_in_millions_1 / 4
    elif (position1 == 2):
        score1 += 2
        score1 += salary_in_millions_1 / 4
    elif (position1 == 3):
        score1 = 0
elif (constructor1 == "Mercedes") or (constructor1 == "Aston Martin"):
    score1 += 1
    if (position1 == 1):
        score1 += 3
        score1 += salary_in_millions_1 / 4
    elif (position1 == 2):
        score1 += 2
        score1 += salary_in_millions_1 / 4
    elif (position1 == 3):
        score1 = 0
elif (constructor1 == "Ferrari"):
    score1 = 0
else:
    if (position1 == 1):
        score1 += 3
        score1 += salary_in_millions_1 / 4
    elif (position1 == 2):
        score1 += 2
        score1 += salary_in_millions_1 / 4
    elif (position1 == 3):
        score1 = 0

if (constructor2 == "Red Bull"):
    score2 += 3
    if (position2 == 1):
        score2 += 3
        score2 += salary_in_millions_2 / 4
    elif (position2 == 2):
        score2 += 2
        score2 += salary_in_millions_2 / 4
    elif (position2 == 3):
        score2 = score2
elif (constructor2 == "McLaren"):
    score2 += 2
    if (position2 == 1):
        score2 += 3
        score2 += salary_in_millions_2 / 4
    elif (position2 == 2):
        score2 += 2
        score2 += salary_in_millions_2 / 4
    elif (position2 == 3):
        score2 = 0
elif (constructor2 == "Mercedes") or (constructor2 == "Aston Martin"):
    score2 += 1
    if (position2 == 1):
        score2 += 3
        score2 += salary_in_millions_2 / 4
    elif (position2 == 2):
        score2 += 2
        score2 += salary_in_millions_2 / 4
    elif (position2 == 3):
        score2 = 0
elif (constructor2 == "Ferrari"):
    score2 = 0
else:
    if (position2 == 1):
        score2 += 3
        score2 += salary_in_millions_2 / 4
    elif (position2 == 2):
        score2 += 2
        score2 += salary_in_millions_2 / 4
    elif (position2 == 3):
        score2 = 0

if(score1 == 0) and (score2 == 0):
    print("Depois de tantas temporadas, o Sainz vai descançar em 2025.")
elif(score1 > score2):
    print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {constructor1}, que pontuou {int(score1)}.")
elif(score2 > score1):
    print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {constructor2}, que pontuou {int(score2)}.")
elif(score1 == score2):
    print("As duas são ótimas opções! Vamos, Sainz!!")