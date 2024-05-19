# Kanye West x Taylor Swift

A relação conturbada entre West e Swift começou há 15 anos, quando ele invadiu o discurso da cantora na cerimônia do Video Music Awards e arrancou o microfone de sua mão, causando um tumulto na indústria musical e deixando uma marca inapagável na história do entretenimento. Desde então, suas carreiras seguiram caminhos divergentes, repletos de altos e baixos, mas a sombra daquela noite de 2009 continuou a pairar sobre eles.

Agora, após uma década e meia, os destinos de West e Swift se cruzam mais uma vez, desta vez no prestigiado Cin Awards. Os dois titãs da música estão mais uma vez competindo.

Os organizadores do Cin Awards, cientes da história tumultuada entre os dois artistas, estão determinados a evitar qualquer controvérsia e garantir uma disputa justa. Para isso, decidiram implementar um novo sistema de votação que seja imparcial, transparente e à prova de manipulação. É aqui que entra em cena o jovem gafanhoto do Cin, com a árdua tarefa de criar esse sistema de avaliação.

## Entrada

Primeiramente, você irá receber um número total de rodadas que irão ocorrer para os juízes avaliarem.

num_rodadas

Em seguida, para cada rodada, você irá receber uma música do Kanye West seguida de 3 avaliações dos juízes.

musica_kanye
avaliacao_kanye1
avaliacao_kanye2
avaliacao_kanye3

Após isso, na mesma rodada, você também irá receber uma música da Taylor Swift seguida de 3 avaliações dos juízes.

musica_taylor
avaliacao_taylor1
avaliacao_taylor2
avaliacao_taylor3

- As avaliações podem ser boa, média, ruim ou péssima.

Cada uma das avaliações dos juízes deve ser considerada e pontuada de acordo com o seguinte:

- boa: +2 pontos
- média: +1 ponto
- ruim: -3 pontos
- péssima: Os fãs expressaram descontentamento, desencadeando uma sequência de entradas de frases de descontentamento aleatórias até que a palavra ORDEM seja recebida. Após a bagunça começar, a cada frase de descontentamento recebida, que seja diferente da palavra ´´ORDEM´´, a pontuação de desordem dos fãs é aumentada em uma unidade, de forma acumulativa.

- Caso a pontuação de desordem do artista alcance um valor maior ou igual a 5 pontos, o respectivo artista perderá o prêmio e o outro será declarado vencedor, indepentemente do número de rodadas restantes.

OBS.1: É importante notar que, mesmo que o artista atinja a pontuação de desordem necessária para causar a sua derrota antes mesmo do fim de todas as avaliações dos juízes, o artista derrotado ainda deverá receber todas as avaliações restantes.

OBS.2: A desordem é acumulativa para cada artista, e não é reinciada em nenhum momento.

OBS.3: Caso um artista, a qualquer momento, já tenha sido matematicamente derrotado devido à desordem dos fãs, então:

- Havendo um outro artista para ser avaliado, não será informada a música, nem haverá avaliação dos juízes para este.
  A sequência de entradas de frases de descontentamento dos fãs ainda deverá continuar sendo recebida até o reestabelecimento da palavra ORDEM.
- Ao final de cada rodada, é necessário verificar qual artista obteve a maior pontuação nesta, acresentando uma vitória ao respectivo artista. Para isso, a pontuação de rodada de ambos os artistas deve ser redefinida automaticamente, de forma que o resultado de uma rodada anterior não influencie as seguintes.

- No entanto, se os artistas finalizarem uma rodada com a mesma pontuação, não haverá acréscimo na contagem de vitórias para nenhum deles. Ou seja, ambos devem permanecer com suas pontuações de vitória inalteradas, e a competição continua normalmente.

- Caso algum dos artistas alcance um total de 3 (três) vitórias durante qualquer momento da competição, este deverá ser declarado vencedor da competição imediatamente, sendo encerrado o Cin Awards - ainda que existam rodadas faltantes.

- Caso o número de rodadas não seja suficiente para que algum dos competidores atinja 3 vitórias, o resultado será determinado de acordo com o artista detentor do maior número de vitórias ao final da competição.

- Em último caso, chegado ao fim da competição com números iguais de vitórias para cada artista, será configurado um empate definitivo.

OBS.4: Não é permitido o uso de break e exit.

## Saída

- Rodadas
  No início de cada rodada, deverá ser mostrado o número da rodada atual:

{rodada}° RODADA:

Ao fim de cada rodada, deverá ser mostrado o vencedor da rodada:

O(a) vencedor(a) da {rodada}° rodada foi {artista_vencedor}

Já em caso de empate na rodada:

Não houve vencedor na {rodada}° rodada

- Desordem

Caso o artista perca a competição devido à desordem dos fãs:

Os fãs do(a) {artista_perdedor} causaram tanta desordem que ele(a) perdeu o prêmio!

E, logo em seguida, para o artista que ganhou a competição devido à desordem dos fãs do seu rival, imprima:

O(a) vencedor(a) do Cin Awards é {artista_vencedor}, parabéns!

- Mérito

Ao fim da competição, caso o artista ganhe por mérito, ou seja, por meio das próprias vitórias:

O(a) vencedor(a) do Cin Awards, com um total de {num_vitorias_do_artista} vitórias, é {artista_vencedor}, parabéns!

Por fim, caso haja um empate em relação ao número final de vitórias dos artistas:

Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!

## Exemplo

| Entrada                                                                                                                                                   | Saída                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 Off The Grid média ruim ruim Ghost Town ruim média média Praise God ruim ruim ruim Peter boa média boa Cassandra boa boa ruim Long Live média boa média | 1° RODADA: O(a) vencedor(a) da 1° rodada foi Taylor Swift 2° RODADA: O(a) vencedor(a) da 2° rodada foi Taylor Swift 3° RODADA: O(a) vencedor(a) da 3° rodada foi Taylor Swift O(a) vencedor(a) do Cin Awards, com um total de 3 vitórias, é Taylor Swift, parabéns! |
