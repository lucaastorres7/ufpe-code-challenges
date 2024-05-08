# Rumo ao Pódio!

Em uma tarde ensolarada no famoso circuito de Monte Carlo, os motores rugem e a competição está bastante acirrada. Três pilotos de elite são favoritos para o grandioso prêmio de Mônaco: Sérgio Leclerc, Riccardo Massa e Calegario Verstappen.

Prestes a participar da corrida mais emocionante da temporada, cada um deles treinou arduamente e agora está pronto para mostrar suas habilidades nas curvas desafiadoras e retas velozes deste lendário circuito e quebrar o recorde de menor tempo da corrida.

Para isso, a equipe de organização da corrida contratou você para auxiliar na criação de um algoritmo responsável por definir o pódio, com base no tempo de corrida realizado por cada piloto a ser apresentado.

Assim, à medida que a bandeira quadriculada se aproxima, a tensão aumenta e os corações aceleram. Quem será coroado o campeão desta emocionante corrida de Fórmula 1? Só o tempo, e o seu código, dirão!

## Entrada

Você irá receber o nome (string) e tempo de finalização da prova (float) dos 3 melhores pilotos, em sequência, da seguinte forma:

piloto_A
tempo_A
piloto_B
tempo_B
piloto_C
tempo_C

Obtidas as informações dos melhores competidores apresentados, você deverá determinar as posições no pódio de cada piloto, verificando os seus respectivos tempos de finalização da corrida. É fundamental entender a lógica por trás da ordenação das variáveis - neste caso, dos tempos de finalização da corrida -, para então determinar o método correto e adequado na comparação dos tempos e, enfim, na decisão de que competidor ficará em qual posição no pódio.

OBS 1: Você deve usar somente operadores lógicos e de comparação, bem como os comandos condicionais aprendidos, para determinar o pódio requisitado pela questão. Dessa forma, está proibido o uso de qualquer outra ferramenta para a construção do pódio, exceto o que foi ensinado na disciplina até o momento.

OBS 2: Considere apenas entradas amigáveis, e que não haverá um cenário de empate (dois ou mais competidores com o mesmo tempo de finalização).

## Saída

- Ao final das comparações, tendo determinado a formação do pódio, deverá imprimir a seguinte mensagem, anunciando o pódio:

E o Pódio do GP de Mônaco é:

- Logo após, deverá imprimir o resultado do pódio:

"{1° Colocado} está no lugar mais alto do pódio com tempo de {tempo do 1° Colocado} horas de corrida."

"{2° Colocado} está no segundo lugar do pódio com tempo de {tempo do 2° Colocado} horas de corrida."

"{3° Colocado} está no terceiro lugar do pódio com tempo de {tempo do 3° Colocado} horas de corrida."

- Ao final, você deve imprimir os sinceros sentimentos do querido comentarista Galvão bueno a respeito do recorde estabelecido.

"Galvão, temos um momento histórico da Fórmula 1, {1° Colocado} acaba de fazer história no GP de Mônaco ao terminar a corrida com {Tempo do 1° Colocado} horas de prova."

## Exemplo

| Entrada                                                           | Saída                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sérgio Leclerc 1.23 Riccardo Massa 1.50 Calegario Verstappen 2.31 | E o Pódio do GP de Mônaco é: Sérgio Leclerc está no lugar mais alto do pódio com tempo de 1.23 horas de corrida. Riccardo Massa está no segundo lugar do pódio com tempo de 1.5 horas de corrida. Calegario Verstappen está no terceiro lugar do pódio com tempo de 2.31 horas de corrida. Galvão, temos um momento histórico da Fórmula 1, Sérgio Leclerc acaba de fazer história no GP de Mônaco ao terminar a corrida com 1.23 horas de prova. |
