total_interviewed = int(input())

approval = 0
bounce = 0
abstention = 0

for i in range (0, total_interviewed):
    resposta = input()
    if(resposta == "Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!"):
        approval += 1
    elif(resposta == "Não gostei. Muito sem graça, onde já se viu nome com duas letras?"):
        bounce += 1
    elif(resposta == "Ainda estou me acostumando. Não tenho uma opinião formada sobre isso."):
        abstention += 1

approval_rate = (approval / total_interviewed) * 100
bounce_rate = (bounce / total_interviewed) * 100
abstention_rate = (abstention / total_interviewed) * 100

print("A pesquisa terminou e os resultados foram os seguintes:")
print(f"Taxa de aprovação: {approval_rate:.2f}")
print(f"Taxa de rejeição: {bounce_rate:.2f}")
print(f"Taxa de abstenção: {abstention_rate:.2f}")

if(approval_rate > bounce_rate):
    print("YES!!! Sabia que as pessoas gostariam!")
elif(approval_rate < bounce_rate):
    print("Ops... Por essa eu não esperava.")
else:
    print("Bom... Vou olhar para o copo meio cheio!")