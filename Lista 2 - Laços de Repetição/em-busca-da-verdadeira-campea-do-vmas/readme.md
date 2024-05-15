# Kanye West: Em busca da verdadeira campeã do VMAs 2009

Aldo, um aluno apaixonado por música pop do Centro de Informática da UFPE, teve uma ideia brilhante: realizar um evento para os fãs de divas pop assistirem juntos ao grandioso Video Music Awards de 2009, um verdadeiro clássico da época dourada da música. No entanto, o que era para ser uma noite de celebração tornou-se palco de intensos debates devido ao famoso incidente entre Kanye West e Taylor Swift naquela noite.

Enquanto todos estavam imersos na emoção do evento, uma discussão acalorada aconteceu quando Kanye West interrompeu o discurso de Taylor Swift, declarando que ela não merecia o prêmio de Melhor Vídeo Musical Feminino, e sim a Beyoncé. Esse momento foi o palco de uma das maiores polêmicas da história do VMA.

Aldo percebeu que seus colegas estavam divididos entre os dois lados da questão: alguns defendiam fervorosamente a elegância e talento de Taylor Swift com "You Belong with Me", enquanto outros não conseguiam negar o poder e o impacto de Beyoncé com "Single Ladies".

Para resolver esse impasse, Aldo criou um algoritmo simples, porém eficaz, que permitia aos presentes no evento do Centro de Informática decidirem de uma vez por todas quem merecia o cobiçado prêmio. Mas claro, havia algumas regras:

- Cada aluno presente no evento terá a oportunidade de expressar sua opinião.
- O algoritmo deve ser imparcial e considerar igualmente todas as opiniões.
- O resultado final será baseado na opinião da maioria dos presentes, mas uma reviravolta pode ocorrer.
- Se houver um empate, haverá uma rodada de debate onde os alunos podem tentar convencer os outros a mudar de voto.
  Após o debate, uma nova votação será realizada e os votos são acumulativos.
- Se ainda houver empate após o debate, o organizador (Aldo) terá o voto decisivo.

## Entrada

- Inicialmente, você recebera a quantidade de alunos no evento:

quantidade_alunos

- Em seguida, você receberá o voto de cada aluno:

"beyonce"
ou
"taylor swift"

- Em caso de empate, você receberá de cada aluno na mesma ordem se ele quer mudar de voto ou não após o debate:

"sim"
ou
"nao"

- Caso o aluno opte por mudar de voto, você deve receber o novo voto dele após o debate:

novo_voto

Lembrete: os votos que mudarem serão acrescentados aos anteriores

- Por fim, se a votação continuar empatada após debate, você receberá o voto decisivo de Aldo:

voto_decisivo

## Saída

- Você precisa imprimir em quem cada aluno votou na primeira votação:

"Aluno {X} votou na Taylor Swift."
ou
"Aluno {X} votou na Beyoncé."

- Após receber todos os votos da primeira seção, imprima a contagem de votos:

"Contagem de votos:"
"Taylor Swift: {qtd_votos_taylor} votos"
"Beyoncé: {qtd_votos_beyonce} votos"

- Em caso de empate, você deve imprimir na fase de debate:

"Empate! Iniciando rodada de debate."
"Alunos, agora é a sua chance de convencer os outros a mudar de voto!"

- Caso o aluno mude o voto na fase de debate, você deve imprimir:

"Aluno {X} mudou seu voto para Taylor Swift."
ou
"Aluno {X} mudou seu voto para Beyoncé."

- Se ocorrer do aluno não mudar o voto após debate, imprima:

"Aluno {X} não mudou seu voto."

- Após coletar os novos votos, imprima:

"Nova contagem de votos após o debate:"
"Taylor Swift: {qtd_votos_taylor} votos"
"Beyoncé: {qtd_votos_beyonce} votos"

- Se houver uma campeã após a primeira contagem ou após a contagem com os novos votos, imprima as seguintes frases:

"Beyoncé venceu com {qtd_votos_beyonce} votos! Será que Kanye West estava certo?"
ou
"Taylor Swift venceu com {qtd_votos_taylor} votos! Kanye West tá irritado com isso."

- Se o empate continuar após o debate, você imprime:

"Aldo, como presidente do evento, tem o voto decisivo."

- Por fim, após o voto decisivo, você imprime a campeã:

"Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso."
ou
"Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?"

## Exemplo

| Entrada                                                     | Saída                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 taylor swift beyonce taylor swift                         | Aluno 1 votou na Taylor Swift. Aluno 2 votou na Beyoncé. Aluno 3 votou na Taylor Swift. Contagem de votos: Taylor Swift: 2 votos Beyoncé: 1 votos Taylor Swift venceu com 2 votos! Kanye West tá irritado com isso.                                                                                                                                                                                                                                                                                                                |
| 2 beyonce taylor swift sim taylor swift sim beyonce beyonce | Aluno 1 votou na Beyoncé. Aluno 2 votou na Taylor Swift. Contagem de votos: Taylor Swift: 1 votos Beyoncé: 1 votos Empate! Iniciando rodada de debate. Alunos, agora é a sua chance de convencer os outros a mudar de voto! Aluno 1 mudou seu voto para Taylor Swift. Aluno 2 mudou seu voto para Beyoncé. Nova contagem de votos após o debate: Taylor Swift: 2 votos Beyoncé: 2 votos Aldo, como presidente do evento, tem o voto decisivo. Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo? |
