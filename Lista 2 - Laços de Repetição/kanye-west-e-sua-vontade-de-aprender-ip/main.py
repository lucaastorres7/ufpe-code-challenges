decisions = int(input())
points = 0

for i in range(0, decisions):
    boas_praticas = input()
    if(boas_praticas == "Códigos limpos e organizados") or (boas_praticas == "Assistir às aulas do REDU") or (boas_praticas == "Tirar dúvidas com os monitores e professores"):
        points += 10
    elif(boas_praticas == "Nomenclatura objetiva e de fácil identificação de variáveis"):
        points += 7
    elif(boas_praticas == "Comentários significativos") or (boas_praticas == "Evitar repetições desnecessárias de códigos"):
        points += 5
    elif(boas_praticas == "Programar utilizando uma boa IDE"):
        points += 3
    elif(boas_praticas == "Programar sem utilizar IDE") or (boas_praticas == "Nomenclatura confusa e difícil de identificar variáveis"):
        points -= 5
    elif(boas_praticas == "Código bagunçado e mal estruturado"):
        points -= 6
    elif(boas_praticas == "Não tirar dúvidas com professores e monitores"):
        points -= 10

if(decisions != 0):
    average = points / decisions

if(points < 0):
    points = 0
    average = points / decisions
elif(decisions == 0):
    average = 0
elif(average > 10):
    average = 10

if(average < 3):
    print("É melhor voltar a cantar mesmo!")
elif(average >= 3) and (average < 7):
    print("Vai precisar se esforçar um pouco mais, meu cantor!")
elif(average == 7):
    print("Na conta certa!")
elif(average > 7) and (average <= 9):
    print("Nasceu para programar!")
elif(average > 9):
    print("Já pode ser chamado de Kanye, the dev, West!")