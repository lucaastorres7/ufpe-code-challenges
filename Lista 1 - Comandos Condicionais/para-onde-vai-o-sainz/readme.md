# Para onde vai o Sainz?

Na Fórmula 1, há 10 construtores competindo, cada um com 2 pilotos e 1 reserva. Carlos Sainz Jr. é um dos 20 pilotos que têm uma posição no grid da temporada de 2024. Porém, o seu construtor, a Ferrari, já assinou um contrato para a temporada de 2025 com o multicampeão Lewis Hamilton, enquanto a outra vaga na equipe está ocupada pelo piloto Charles Leclerc.

Por isso, Sainz precisa assinar um novo contrato, ou entrará em ano sabático.

Para facilitar esse processo e a sua decisão, Sainz precisa de um programa que receba duas propostas de contrato e decida qual é a melhor entre elas, e, portanto, a que ele deverá escolher.

Com o objetivo de definir critérios claros na comparação entre propostas, Sainz criou um sistema de pontuação baseado na “posição” dentro da equipe, no salário e no construtor. A melhor proposta será definida, então, de acordo com a proposta que obtiver a maior pontuação.

OBS: Ele pode receber a proposta de qualquer um dos construtores, mas ele só a considerará se o assento for para primeiro ou segundo piloto, ou se for reserva da Red Bull - caso contrário, a proposta deve ser rejeitada, independentemente da sua pontuação. Além disso, se a proposta for da Ferrari, também deverá ser recusada.

Se o construtor for Red Bull, some 3, se for McLaren, some 2, e se for Mercedes ou Aston Martin, some 1.. Se a posição for 1, some 3 à pontuação, e se a posição for 2, some 2. Por fim, se a posição não for 3, some o quociente (resultado) da divisão inteira da sétima ordem (casa dos milhões) do salário por 4.

## Exemplo

Entrada (Proposta):

Aston Martin
2
5
(...)

O construtor é a Aston Martin, então adicionamos 1 aos pontos da proposta. A posição ofertada é a segunda, então vamos somar mais 2 pontos. Como não é a posição de reserva (3), o salário influenciará na escolha, e por isso faremos 5 // 4 (divisão inteira de 5 por 4) e somamos o resultado à pontuação, totalizando 4 pontos.

Você deve usar apenas comandos condicionais (if, elif e else), operadores lógicos (and, or e not) e de comparação para resolver esse problema.

## Entrada

A entrada consiste em 3 linhas para cada proposta:

Construtor1
Posição1
Salário1

Construtor2
Posição2
Salário2

O construtor consiste no nome da equipe que está fazendo a proposta, a posição pode ser 1, 2 ou 3 (reserva), e o salário será o valor da proposta em milhões (se for 12 milhões, por exemplo, a entrada será 12).

## Saída

- Se Sainz não aceitar nenhuma das propostas, imprima:

"Depois de tantas temporadas, o Sainz vai descançar em 2025."

- Se aceitar apenas uma, a saída deve ser:

"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor}, que pontuou {pontos}."

- Se as duas propostas pontuarem igualmente e ambas forem aptas, a saída deve ser:

"As duas são ótimas opções! Vamos, Sainz!!"

## Exemplo

| Entrada               | Saída                                                            |
| --------------------- | ---------------------------------------------------------------- |
| Haas 2 12 Sauber 1 12 | SMOOOOTH OPERATOOR! Sainz vai correr pela Sauber, que pontuou 6. |
| Haas 3 2 McLaren 3 9  | Depois de tantas temporadas, o Sainz vai descançar em 2025.      |
