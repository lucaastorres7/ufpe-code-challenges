# Kanye West e Sua Vontade de Aprender IP

Após uma carreira musical de sucesso com muitos shows ao redor do mundo e músicas em alta, Kanye West decide finalmente em seguir seu sonho e carreira que tanto queria em toda sua vida: se mudar para Recife e ser aluno do CIn para aprender IP no GRAD 5!

Após várias tentativas de entrada, o músico e agora novo programador em formação entra no CIn e não vê a hora de começar seus estudos.

Para se sair bem na disciplina, Kanye precisa de sua ajuda, grandioso(a) aluno(a) de IP!

Você precisará informar quais decisões o cantor e futuro programador deve (e não deve) tomar em relações às boas práticas de programação e de estudo da disciplina para que seja um ótimo aluno, assim como você.

As boas práticas levadas em consideração são:

- Programar utilizando uma boa IDE —> 3 pontos
- Códigos limpos e organizados —> 10 pontos
- Nomenclatura objetiva e de fácil identificação de variáveis —> 7 pontos
- Assistir às aulas do REDU —> 10 pontos
- Comentários significativos —> 5 pontos
- Evitar repetições desnecessárias de códigos —> 5 pontos
- Tirar dúvidas com os monitores e professores —> 10 pontos

As más práticas levadas em consideração são:

- Programar sem utilizar IDE —> -5 pontos
- Código bagunçado e mal estruturado —> -6 pontos
- Nomenclatura confusa e difícil de identificar variáveis —> -5 pontos
- Não tirar dúvidas com professores e monitores —> -10 pontos

## Entrada

Serão n decisões que gerarão pontos que vão prever o desempenho do ilustre novo aluno na disciplina.

Portanto, a primeira linha de entrada será um número inteiro que vai identificar a quantidade de boas práticas a serem medidas:

n

As seguintes n linhas de entrada serão as práticas de programação (podendo ser boas ou más) levadas em consideração que deixarão Kanye um mestre em IP:

boa_pratica_1
boa_pratica_2
…
boa_pratica_n

## Saída

Por fim deve-se fazer uma média aritmética da pontuação obtida com as práticas de programação recebidas e apresentar as seguintes mensagens:

OBS: Se a soma das pontuações for negativa, atribuir 0 à pontuação total.

OBS: Se .o número de n linhas for zero, deve-se considerar que a média de Kayne foi zero.

OBS: Se a média for acima de 10, atribuir 10 à media. Faça isso depois de extrair a média aritmética.

- Caso a media seja menor que 3, apresentar na tela:

‘É melhor voltar a cantar mesmo!’

- Caso a media seja maior ou igual a 3 e menor que 7, apresentar na tela:

‘Vai precisar se esforçar um pouco mais, meu cantor!’

- Caso a media seja igual a 7, apresentar na tela:

‘Na conta certa!’

- Caso a media seja acima de 7 e menor ou igual a 9, apresentar na tela:

‘Nasceu para programar!’

- Caso a media seja acima de 9, apresentar na tela:

‘Já pode ser chamado de Kanye, the dev, West!’

## Exemplo

| Entrada                                                                                                                                                                                                              | Saída                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| 4 Programar utilizando uma boa IDE Assistir às aulas do REDU Código bagunçado e mal estruturado Tirar dúvidas com os monitores e professores                                                                         | Vai precisar se esforçar um pouco mais, meu cantor! |
| 5 Evitar repetições desnecessárias de códigos Tirar dúvidas com os monitores e professores Código bagunçado e mal estruturado Nomenclatura objetiva e de fácil identificação de variáveis Programar sem utilizar IDE | É melhor voltar a cantar mesmo!                     |
