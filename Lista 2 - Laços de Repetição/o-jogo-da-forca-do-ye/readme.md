# O Jogo da Forca do Ye!

O Kanye West estava trabalhando em seus projetos quando de repente surge um enorme interesse em adentrar no mundo da programação!

Com isso, Kanye começa a estudar Python e tem a ideia de criar um jogo da forca com o nome de suas músicas. Mas, devido ao seu trabalho musical, não está tendo tempo suficiente para continuar programando o jogo.

Por isso, Kanye contrata ninguém menos do que você para ajudá-lo a criar o jogo dele!

Kanye deixa bem claro o que você deve fazer no jogo: o usuário deverá receber um número N de músicas famosas do Kanye West. De acordo com o tamanho do nome da música, o usuário possui um número de tentativas igual ao dobro do número de letras da música (sem contar espaços em branco, caso o nome da música possuir mais de uma palavra).

Após isso, o usuário deverá chutar letras até que ele acerte a música misteriosa ou até que a quantidade de chutes acabe.

OBS: inicialmente, você deve atualizar a palavra de modo que a cada letra deverá ter um ‘\_’.

- Exemplos:
  Se a música for STRONGER, inicialmente a resposta do usuário será **\_\_\_\_** (8 underlines) caso o usuário erre o chute

Se a música for I WONDER, inicialmente a resposta do usuário será \_ **\_\_** (7 underlines totais) caso o usuário erre o chute

Toda vez que o usuário acertar um chute, a letra do chute deverá ser atualizada na sua resposta.

- Exemplo:
  Se a música era STRONGER e o chute foi O, então a resposta do usuário vai ser atualizada de **\_\_\_\_** para **\_ O\_\_**

Se a música for HEARTLESS e o chute foi S, então a resposta do usuário vai ser atualizada de \***\*\_\*\*** para **\_\_\_**SS

Ao final do código, deverá ser calculada uma taxa de acertos das músicas acertadas pelo usuário em relação ao total de músicas.

OBS:

- Não é permitido usar break no código;
- Todos os inputs dos nomes de música virão com as letras maiúsculas, bem como os inputs dos chutes.

## Entrada

A primeira entrada do código deverá ser um número inteiro N que representa o número de músicas que o usuário deve descobrir.

- Exemplo:
  2

Após isso, serão recebidas N entradas contendo nomes de músicas (strings) do Kanye West.

- Exemplos:
  FLASHING LIGHTS
  STRONGER

A cada entrada de música serão recebidas entradas de chutes, que são letras.

- Exemplos:
  A
  B

## Saída

A primeira saída deverá ser printada sempre no começo:

Bem vindo ao jogo da forca do ye!

Após isso, cada vez que receber uma entrada de música, printe qual sua ‘posição’ em relação às outras músicas e em relação ao total de músicas:

- Caso ela não seja a última música, printe:

Esta é a música {musica_atual} de {numero_de_musicas}.

- Caso contrário, printe:

Última música!

Se o usuário chutar uma letra que não está no nome da música, printe:

Eita! Parece que a letra {chute} não está na música secreta!

Caso contrário:

- Se o usuário chutou uma letra e ele ainda não havia acertado, printe:

Uhuuuuu! Consegui adivinhar uma letra!

- Se o usuário chutou uma letra que ele já havia acertado, printe:

Já tinha colocado essa letra antes, preciso de mais atenção.

Para cada chute, independente de ser um chute certo ou errado, o programa deverá printar a situação atual da resposta do usuário:

Resposta atual: {minha_resposta}

Se o usuário conseguiu acertar a música antes que a quantidade de tentativas chegasse à zero, printe:

Isso! Consegui acertar uma música!

Caso contrário, printe:

Vish, essa tava difícil, a música era {nome_musica}. Espero acertar a próxima!

Após a quantidade de músicas acabarem, o programa deve printar quantas músicas o usuário acertou em relação ao número total de músicas:

Consegui acertar {total_de_pontos} músicas de {numero_de_musicas}!

Logo após, printe de acordo com à taxa de acertos do usuário:

- Se a taxa de acertos for inferior ou igual à 50%, printe:

Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!

- Se a taxa de acertos for superior à 50% e inferior ou igual à 75%, printe:

Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.

- Se a taxa de acertos for superior à 75% e inferior à 100%, printe:

Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.

- Se a taxa de acertos for 100%, printe:

Eu sou o próprio Kanye West.

## Exemplo

| Entrada                  | Saída                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 FAMOUS F A E A M O U S | Bem vindo ao jogo da forca do ye! Última música! Uhuuuuu! Consegui adivinhar uma letra! Resposta atual: F**\_** Uhuuuuu! Consegui adivinhar uma letra! Resposta atual: FA\_**\_ Eita! Parece que a letra E não está na música secreta! Resposta atual: FA\_\_** Já tinha colocado essa letra antes, preciso de mais atenção. Resposta atual: FA\_**_ Uhuuuuu! Consegui adivinhar uma letra! Resposta atual: FAM_** Uhuuuuu! Consegui adivinhar uma letra! Resposta atual: FAMO\__ Uhuuuuu! Consegui adivinhar uma letra! Resposta atual: FAMOU_ Uhuuuuu! Consegui adivinhar uma letra! Resposta atual: FAMOUS Isso! Consegui acertar uma música! Consegui acertar 1 músicas de 1! Eu sou o próprio Kanye West. |
