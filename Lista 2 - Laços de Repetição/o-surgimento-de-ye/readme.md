# O Surgimento de Ye

Kanye West, renomado rapper e produtor musical, tomou a decisão de mudar legalmente seu nome artístico para "Ye", um apelido pelo qual ele já era conhecido há anos. Essa mudança reflete não apenas sua evolução musical, mas também seu desejo de simplificar sua identidade pública e se conectar mais intimamente com seu público.

No entanto, ele não tem certeza de como seu público reagiu a essa mudança. Por isso, você, aluno do CIn, irá ajudá-lo criando um programa para ouvir a opinião das pessoas sobre essa mudança.

## Entrada

O input inicial será um número inteiro N que representa quantas pessoas serão entrevistadas.

N (int)

- Depois, você irá registrar uma resposta para cada pessoa entrevistada:

Resposta1
Resposta2
Resposta3
.(...)
RespostaN

- Para cada uma delas, existirão 3 tipos de respostas possíveis:

"Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!"

"Não gostei. Muito sem graça, onde já se viu nome com duas letras?"

"Ainda estou me acostumando. Não tenho uma opinião formada sobre isso."

## Saída

Logo após receber todas as respostas, você deve anunciar o resultado da pesquisa:

"A pesquisa terminou e os resultados foram os seguintes:"

- Em seguida, deve imprimir as estatísticas da seguinte forma:

"Taxa de aprovação: {taxa_aprovacao}"
"Taxa de rejeição: {taxa_rejeicao}"
"Taxa de abstenção: {taxa_abstencao}"

OBS.1.: As casas decimais das taxas devem ser limitadas em duas.
Dica: Para calcular as taxas, você deve fazer os cálculos da seguinte maneira:

Para taxa de aprovação: (aprovados / totais) _ 100
Para taxa de rejeição: (rejeicao / totais) _ 100
Para taxa de abstenção: (abstencao / totais) \* 100

OBS.2: O valor totais consiste na soma das 3 possibilidades de resposta.

- Depois disso, caso a taxa de aprovação seja maior que a de rejeição, você deve imprimir:

"YES!!! Sabia que as pessoas gostariam!"

- No entanto, caso a de rejeição seja maior, imprima:

"Ops... Por essa eu não esperava."

- Por fim, caso as taxas de aprovação e rejeição sejam iguais:

"Bom... Vou olhar para o copo meio cheio!"

## Exemplo

| Entrada                                                                                                                                                                                             | Saída                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!! Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!! Ainda estou me acostumando. Não tenho uma opinião formada sobre isso. | A pesquisa terminou e os resultados foram os seguintes: Taxa de aprovação: 66.67 Taxa de rejeição: 0.00 Taxa de abstenção: 33.33 YES!!! Sabia que as pessoas gostariam! |
