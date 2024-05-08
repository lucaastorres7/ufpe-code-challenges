weather = input() # ensolarado, nublado e chuvoso.

if(weather == "chuvoso"):
    wet_track = input()
    if(wet_track == "True"):
        wet_track_bool = True
    elif(wet_track == "False"):
        wet_track_bool = False

track_temperature = input() # alta, moderada e baixa.
training_performance = input() # bom ou ruim.
starting_position = int(input()) # 1 to 20

print("Estratégia de prova de Max Verstappen!")

if(weather == "ensolarado") and (track_temperature == "alta"):
    print("Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!")
elif(weather == "ensolarado") and (track_temperature != "alta"):
    print("Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.")
elif(weather == "nublado") and (track_temperature == "alta"):
    print("Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!")
elif(weather == "nublado") and (track_temperature != "alta"):
    print("Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!")
elif(weather == "chuvoso") and (wet_track_bool == True):
    print("Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.")
elif(weather == "chuvoso") and (wet_track_bool == False):
    print("Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!")

if(starting_position == 1) and (training_performance == "bom"):
    print("Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.")
elif(starting_position == 1) and (training_performance == "ruim"):
    print("Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.")
elif(starting_position != 1) and (starting_position <= 12):
    print("Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.")
elif(starting_position > 12):
    print("Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.")