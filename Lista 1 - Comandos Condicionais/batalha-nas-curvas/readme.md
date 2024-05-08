# Batalha nas Curvas 🏎️

Em uma emocionante competição de Fórmula 1, o vencedor é determinado pela pontuação acumulada ao longo de várias corridas. A última corrida definirá o resultado final entre os três principais competidores.

Sua missão é anunciar o vencedor com base nas pontuações dos pilotos. Os três principais pilotos são:

- Lewis Hamilton
- Max Verstappen
- Valtteri Bottas

## Entrada

Haverá 6 entradas de números inteiros, correspondendo à pontuação acumulada do piloto na competição e a colocação de cada piloto na última corrida que aconteceu, na seguinte ordem:

- Pontuação acumulada de Lewis Hamilton
- Colocação de Lewis Hamilton na última corrida
- Pontuação acumulada de Max Verstappen
- Colocação de Max Verstappen na última corrida
- Pontuação acumulada de Valtteri Bottas
- Colocação de Valtteri Bottas na última corrida

OBS: Caso o piloto esteja entre os 10 primeiros colocados na última corrida, a pontuação acumulada dele é acrescida em 5 pontos.

OBS: Em caso de empate na pontuação acumulada, o desempate é feito considerando a ordem alfabética dos nomes dos pilotos.

## Saída

A saída será uma única linha anunciando o vencedor com base na pontuação acumulada:

"X ganhou a competição com Y pontos!"

Onde X é o nome do piloto vencedor e Y é a sua pontuação acumulada.

## Exemplo

| Entrada        | Saída                                             |
| -------------- | ------------------------------------------------- |
| 25 1 18 2 15 3 | Lewis Hamilton ganhou a competição com 30 pontos! |
| 10 4 15 2 15 3 | Max Verstappen ganhou a competição com 20 pontos! |
