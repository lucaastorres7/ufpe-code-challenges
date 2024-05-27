# Quem pegou minha tinta?

Após chegar em casa, a bruxa percebeu que sua tinta mágica foi roubada, e logo suspeitou do seu ex-marido, o feiticeiro. Contudo, não encontrou nenhum possível rastro de magia, o que a levou a pensar que ele poderia ter convencido alguém a fazer essa atrocidade em seu lugar.

Para tentar descobrir o mais rápido possível os possíveis culpados pelo roubo da sua valiosa tinta, a poderosa bruxa resolveu pedir para que você, um brilhante programador, organizasse uma lista de suspeitos que teriam conseguido passar despercebidos pelo seu fiel ajudante duende.

Para isso, você deverá receber diversas entradas, sem um fim bem definido, que deverão determinar a construção da lista de suspeitos. Pense com cuidado e ajude a bruxa a resolver esse mistério!

## Entrada

Para cada entrada abaixo, realize a respectiva ação associada:

"Novo suspeito - altíssima periculosidade"

- Receba como entrada um nome (string) e o adicione no começo da lista.

"Novo suspeito - pouco perigoso"

- Receba como entrada um nome (string) e o adicione no final da lista.

"Livre de suspeita, pode remover"

- Receba como entrada um nome (string) e o remova da lista.

"Sujeito mais perigoso do que pensávamos"

- Receba duas entradas, respectivamente: uma com o índice atual do sujeito na lista, e outra com o índice a ser atualizado. Troque a posição do indivíduo na lista com o indivíduo que está na nova posição dele a partir disso.
- OBS.1: Os índices (inteiro) estarão no intervalo de 0 à N - 1, sendo N o tamanho da lista.

"Que estranho, esses dois meliantes… troque-os de lugar"

- Receba duas entradas, cada uma contendo um nome (string), e inverta a posição deles na lista.

"Essa posição não esta de acordo, ele não e tão perigoso assim"

- Receba uma entrada contendo um nome (string), e atualize a lista levando o nome do sujeito para o final da lista.

"Como a lista esta ficando?"

- Não recebe entrada, apenas imprime todos os nomes da lista, conforme especificado no output.

"Já temos nossa lista de suspeitos"

- Finaliza o recebimento de entradas, e imprime uma resposta, conforme especificado no output.

OBS.2: Nunca existirão duas ou mais pessoas com o mesmo nome na lista.
OBS.3: As entradas serão amigáveis, seguindo sempre as especificações acima.

## Saída

- Caso a entrada seja "Como a lista esta ficando?", você deve imprimir a lista de suspeitos da seguinte forma:
  suspeito1, suspeito2, suspeito3, (...), suspeitoN

- Caso a entrada seja "Ja temos nossa lista de suspeitos", imprima:

O resultado final ficou assim:
suspeito1, suspeito2, suspeito3, (...), suspeitoN

OBS.4: Em ambos os casos, é preciso imprimir os nomes de todos os suspeitos separados por uma virgula e um espaço em branco, e na mesma ordem que estão na lista.

## Exemplo

| Entrada                                                                                                                                                                                                                                                                                                                                                                                       | Saída                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Novo suspeito - altíssima periculosidade Pedro Novo suspeito - pouco perigoso Welton Como a lista esta ficando? Novo suspeito - altíssima periculosidade Luana Como a lista esta ficando? Que estranho, esses dois meliantes… troque-os de lugar Pedro Luana Como a lista esta ficando? Essa posição não esta de acordo, ele não e tão perigoso assim Luana Já temos nossa lista de suspeitos | Pedro, Welton Luana, Pedro, Welton Pedro, Luana, Welton O resultado final ficou assim: Pedro, Welton, Luana |
