# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

**Nome:**

> Firewall.IA

## 2. Integrantes do grupo

- Nome 1: Raiany Morais
- Nome 2: Sávio José Salomão 
- Nome 3: Charles Oliveira

## 3. Tema escolhido

**Tema:**

> Inteligência Artificial no Cotidiano: Confiabilidade de sistemas inteligentes, segurança e análise crítica de dados.

**Como esse tema se relaciona com o jogo?**

> O jogador assume o papel de uma IA responsável por validar cadastros de usuários. O tema define diretamente as regras e os desafios da partida: o jogador precisa analisar criticamente cada ficha para diferenciar usuários legítimos, erros simples de preenchimento e tentativas maliciosas de invasão por código, garantindo a confiabilidade e a segurança do sistema sem bloquear injustamente pessoas comuns.

## 4. Tipo de jogo

**Tipo escolhido:**

> RPG de decisão e triagem (perguntas, respostas e análise de fichas).

## 5. Descrição geral do jogo

**Descrição:**

> Antes de iniciar a partida, uma tela inicial exibe as regras de validação do sistema. Durante o jogo, aparecem na tela fichas cadastrais de usuários (contendo campos como nome, idade e CEP) junto com três opções de decisão: Válido, Inválido e Bloqueado. O jogador controla o sistema de triagem e precisa analisar os dados de cada ficha para tomar a decisão correta, enfrentando o desafio de identificar erros de digitação e tentativas de invasão hacker (como linhas de código inseridas nos campos). O jogo conta com um sistema de pontuação acumulada a cada acerto e exibe uma tela final de desempenho ao término de todos os casos.

## 6. Objetivo do jogador

**Objetivo:**

> O jogador trabalha como uma IA, validando sistemas de fichas de identidade, o seu objetivo é validar fichas corretas, invalidar fichas com dados errados e bloquear hackers que tentarem invadir o sistema.


## 7. Regras principais

- O jogador escolherar entre três opções: valido, invalido e bloqueado. 

- Cada partida receberá uma quantidade de pontos; porém, se validar usuários inválidos, ele não receberá pontos, mas a partida continua e os pontos de usuários válidos vão ser contados. Porém, se o jogador aceitar um hacker, ele perde todos os pontos da partida.

- A partida termina quando os casos acaba.

- Na tela do jogador, antes de ele entrar na partida, aparecerá uma página contendo as regras: só validar usuários com fichas corretas; invalidar usuários com a ficha errada (ou seja, quando no lugar do nome estiverem escritos números, nomes no campo errado ou palavras e nomes errados.); e bloquear usuários em que, no lugar do campo, estiver escrita uma linha de código, por exemplo: if true.


## 8. Condição de vitória

**Condição de vitória:**

> Concluir a análise de todas as fichas da partida sem permitir que nenhum hacker invada o sistema. Se todas as fichas forem classificadas corretamente, o jogador recebe a mensagem: "Você protegeu o sistema e validou da maneira correta". Caso proteja o sistema contra hackers, mas tenha aprovado fichas com erros simples, recebe: "Você protegeu o sistema, porém não validou da forma correta".

## 9. Condição de derrota ou encerramento

**Condição de derrota ou encerramento:**

> A partida é encerrada quando todos os casos da rodada forem avaliados. Se o jogador tiver validado a ficha de algum hacker durante a partida, ocorre falha de segurança, ele perde os pontos acumulados e a tela final exibe: "VOCÊ DEIXOU O SISTEMA SER INVADIDO".

## 10. Elementos previstos no jogo

- **Personagem ou elemento principal:** Sistema de Inteligência Artificial de validação (cursor/seletor de decisão controlado pelo jogador).
- **Obstáculos ou desafios:** Fichas de usuários com dados inconsistentes (erros de digitação) e fichas maliciosas contendo injeção de código de hackers.
- **Itens ou objetos de interação (se houver):** Fichas cadastrais exibidas na tela e botões/opções de escolha (Válido, Inválido e Bloqueado).
- **Pontuação, vidas, tempo ou progresso:** Sistema de pontuação por acertos e contador de progresso das fichas analisadas na rodada.

## 11. Controles previstos

**Controles:**

> Escolher uma das opções com as setas direcionais (para cima e para baixo) ou utilizando o mouse, e confirmar a opção apertando a tecla Enter (ou clique do mouse).

## 12. Principais dificuldades esperadas

- Dificuldade 1: Organizar a interface gráfica e o alinhamento dos textos das fichas e botões de forma clara no Pygame.
- Dificuldade 2: Estruturar a leitura dos casos usando listas e dicionários.
- Dificuldade 3: Implementar os testes unitários das funções de validação.

## 13. Escopo mínimo para a entrega final

**Escopo mínimo:**

> Uma tela inicial com as regras do jogo, uma tela principal funcional exibindo uma sequência fixa de fichas (carregadas de uma lista ou arquivo), controles pelo teclado/mouse para selecionar entre Válido, Inválido e Bloqueado, cálculo de pontuação e uma tela final apresentando uma das três mensagens de resultado conforme o desempenho do jogador.

## 14. Possíveis melhorias, caso haja tempo

- Melhoria 1: Adicionar efeitos sonoros para acertos, erros e alerta de invasão hacker.
- Melhoria 2: Implementar um sistema de ranking salvando as melhores pontuações em arquivo.
- Melhoria 3: Adicionar um temporizador por ficha ou níveis de dificuldade com dados mais sutis para analisar.

