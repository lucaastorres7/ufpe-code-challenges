print("Bem vindo ao jogo da forca do ye!")
music = int(input())
wins = 0

for i in range(music):
  song = input()

  if(i == music - 1):
    print("Última música!")
  else:
    print(f"Esta é a música {i+1} de {music}.")

  hangman = ""
  song_without_spaces = "".join(song.split())
  attempts = len(song_without_spaces) * 2
  right_letters = ""

  for j in song:
    if(j == " "):
      hangman += " "
    else:
      hangman += "_"

  k = 0
  while (k < attempts):
    guess = input()
    new_hangman = ""

    for j in range(len(song)):
      if(guess == song[j]) or (hangman[j] != "_"):
        new_hangman += song[j]
      else:
        new_hangman += "_"

    hangman = new_hangman

    if(guess not in song):
      print(f"Eita! Parece que a letra {guess} não está na música secreta!")
      print("Resposta atual:")
      print(hangman)
    elif(guess in song) and (guess not in right_letters):
      print("Uhuuuuu! Consegui adivinhar uma letra!")
      print("Resposta atual:")
      print(hangman)
    elif(guess in song) and (guess in right_letters):
      print("Já tinha colocado essa letra antes, preciso de mais atenção.")
      print("Resposta atual:")
      print(hangman)
    
    if(guess in hangman):
      right_letters += guess
    
    if(song == hangman):
      print("Isso! Consegui acertar uma música!")
      wins += 1
      k = attempts
      continue
    k += 1
    if(k >= attempts):
      print(f"Vish, essa tava difícil, a música era {song}. Espero acertar a próxima!")

print(f"Consegui acertar {wins} músicas de {music}!")

percentage = (wins / music) * 100
if(int(percentage) <= 50):
  print("Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!")
elif(int(percentage) > 50) and (int(percentage) <= 75):
  print("Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.")
elif(int(percentage) > 75) and (int(percentage < 100)):
  print("Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.")
elif(int(percentage) == 100):
  print("Eu sou o próprio Kanye West.")