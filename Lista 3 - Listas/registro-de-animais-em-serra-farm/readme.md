# Registro de Animais em Serra Farm

No fantástico mundo de Stardew Valley, popular RPG de aventura em mundo aberto, temos uma infinidade de tipos de animais que os jogadores podem ter em suas fazendas. Sejam eles de estimação ou não, todos têm suas peculiaridades e importância no ecossistema da fazenda, e existe sempre um grande interesse em obter e monitorá-los, uma vez que a perda deles é possível.

Filipe, um jogador novato em Stardew Valley, acaba de se tornar o mais novo membro de Serra Farm, a fazenda construída em cooperação com os seus amigos do CIn. Para que fosse estimulado a conhecer por conta própria os ambientes dessa incrível fazenda, seus grandes amigos Lucas e Dantas, conhecedores natos das maravilhas de Serra Farm, fazem o seguinte pedido: construir um catálogo dos primeiros animais que encontrasse na caminhada que inaugura seu primeiro dia no jogo.

Para isso, Filipe precisará da sua ajuda, um brilhante estudante de IP. Sua tarefa será construir um programa em Python que deve funcionar como um sistema de registro de animais em um catálogo bastante simples, adicionando os nomes dos animais encontrados em sequência por Filipe.

## Entrada

Inicialmente, o programa deverá receber o número desejado de animais que o catálogo deverá registrar:

num_animais (inteiro)

OBS.1: Não é necessário considerar casos em que o número de animais seja zero, isso nunca acontecerá.

Enquanto o catálogo não possuir o número desejado de animais, você receberá, por um número indeterminado de vezes, um comando como entrada:

comando (string)

As possibilidades de comando, bem como o que deve ser feito em seu acionamento, são as seguintes:

1. REGISTRA

- Faz o registro do nome de um animal encontrado;
- Caso o mesmo animal já tenha sido catalogado antes, este não deverá ser registrado novamente.

2. CORRIGE

- Apaga o registro do último (mais recente) animal catalogado.

3. REINICIA

- Redefine o catálogo do zero, apagando o registro de todos os animais catalogados anteriormente.
- No caso do comando acionado ser ”REGISTRA”, o programa deverá receber o nome do animal logo em seguida:

animal (string)

## Saída

- Caso o comando acionado seja ”REGISTRA”:
  Se o animal recebido na entrada já estava registrado no catálogo, imprima:

{animal} já foi registrado antes!

Caso contrário:

{animal} registrado com sucesso.

- Caso o comando acionado seja ”CORRIGE”:
  Se existe pelo menos um animal no catálogo, imprima:

Último registro apagado com sucesso.

Caso contrário:

O catálogo ainda está vazio.

- Caso o comando acionado seja ”REINICIA”:
  Independentemente da situação atual do catálogo, imprima:

Catálogo redefinido com sucesso.

Ao final, quando o catálogo tiver sido preenchido por completo, anuncie que o registro foi finalizado com sucesso:

Todos os animais foram registrados!

Logo depois, faça uma quebra de linha adicional, e imprima o catálogo de animais da seguinte forma:

Catálogo de animais:
1º: {animal_1}
2º: {animal_2}
3º: {animal_3}
(...)
{N}º: {animal_N}

OBS.2: A ordem dos animais na impressão do catálogo deverá seguir a ordem em que foram registrados.

## Exemplo

| Entrada                                                                | Saída                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4 REGISTRA Galinha REGISTRA Pato REGISTRA Coelho REGISTRA Vaca         | Galinha registrado com sucesso. Pato registrado com sucesso. Coelho registrado com sucesso. Vaca registrado com sucesso. Todos os animais foram registrados! Catálogo de animais: 1º: Galinha 2º: Pato 3º: Coelho 4º: Vaca                   |
| 2 REGISTRA Cabra REGISTRA Cabra CORRIGE REGISTRA Ovelha REGISTRA Porco | Cabra registrado com sucesso. Cabra já foi registrado antes! Último registro apagado com sucesso. Ovelha registrado com sucesso. Porco registrado com sucesso. Todos os animais foram registrados! Catálogo de animais: 1º: Ovelha 2º: Porco |
