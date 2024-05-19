# Kanye para Presidente

Após mais de 20 anos na indústria musical, Kanye West resolveu se candidatar à presidência dos Estados Unidos durante as eleições que ocorreram no ano de 2020. Contudo, o cantor não obteve sucesso em sua primeira empreitada, obtendo pouquíssimos votos naquela ocasião.

Esse fracasso eleitoral, por outro lado, não impediu Kanye de continuar em busca do seu sonho de tornar-se o primeiro rapper a ocupar o cargo de presidente de uma das mais importantes nações mundiais. Neste ano de 2024, ele está se articulando para tentar novamente uma vitória no pleito, prevendo uma maior adesão dos eleitores em relação a sua primeira tentativa.

Suspeitando que seus oponentes políticos estariam tentando sabotar seus possíveis votos na futura eleição, Kanye pediu para que você, estudante do CIn, desenvolva um programa responsável por calcular o resultado eleitoral sem eventuais interferências.

## Entrada

Inicialmente, seu programa deverá receber diversos números inteiros, em sequência:

N1
N2
N3
(...)
Ni

Sendo Ni o i-ésimo número inteiro recebido como entrada.

Cada valor numérico recebido representa um tipo de bloco de votos, caracterizado por pesos diferentes, a serem computados para um candidato nas eleições.

Para determinar o número exato de votos contidos no bloco, temos as seguintes regras:

- Para cada número divisível por 7, mas não por 2, Kanye West receberá 20 milhões de votos.
- Para cada número divisível por 2, mas não por 7, Kanye West receberá 10 milhões de votos.
- Para cada número não divisível por ambos (2 e 7), 14 milhões de votos serão computados para outros candidatos.

O programa deverá encerrar a leitura dos valores numéricos quando a entrada recebida for a seguinte:

“FIM”

Além disso, caso o número total de votos computados na eleição atinja o patamar dos 300 milhões de votos em qualquer momento durante o recebimento dos blocos de voto, a leitura dos valores numéricos de entrada também deverá ser interrompida imediatamente - ainda que o input "FIM" não tenha sido recebido até então.

## Saída

- No primeiro turno, caso Kanye consiga obter mais de 170 milhões de votos, ele estará matematicamente eleito como presidente, e o programa deverá imprimir:

“O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.”

- Por outro lado, caso Kanye não consiga obter o mínimo de 130 milhões de votos, você deverá imprimir:

“Caramba, não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.”

- Por fim, se houver alcançado um resultado entre 130 e 170 milhões de votos, deverá ser realizada uma nova votação, em segundo turno, sendo anunciada:

“A eleição está disputada, vamos ter um segundo turno!”

ATENÇÃO: Iniciado o segundo turno, o programa deverá executar mais uma etapa de recebimento de blocos de votação, seguindo o mesmo funcionamento do primeiro turno.

- Durante o segundo turno, caso o rapper supere os 170 milhões de votos, o programa deverá imprimir:

“Depois de um pleito muito acirrado, O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.”

- Caso contrário, imprima:

“Caramba, foi uma disputa muito acirrada, mas não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.”

- Além disso, ao final de cada turno, independentemente do resultado obtido, você deverá anunciar os números obtidos pelo cantor:

“Kanye conseguiu ao final da campanha um total de {quantidade_votos_kanye} votos.”

OBS.: Os votos totais ao final da campanha consistem nos votos obtidos exclusivamente no último turno realizado.

## Exemplo

| Entrada                                                    | Saída                                                                                                                                                                           |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 12 21 35 49 63 77 12 FIM                                   | Caramba, não foi dessa vez pro Kanye, voltaremos mais fortes na próxima. Kanye conseguiu ao final da campanha um total de 120000000 votos.                                      |
| 21 35 49 63 77 91 105 119 133 147 161 175 12 8 16 18 22 24 | O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira. Kanye conseguiu ao final da campanha um total de 300000000 votos. |
