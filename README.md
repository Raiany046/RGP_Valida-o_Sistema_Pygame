# RPG: Validação_de_sistema

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Raiany Morais
- Charles Oliveira
- Moises Do Carmo

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

O jogador atua como uma IA de segurança e triagem, analisando fichas de identidade de usuários em tempo real. O objetivo é aprovar fichas legítimas, rejeitar fichas com dados inconsistentes ou mal preenchidos e bloquear tentativas de ataque de hackers, garantindo a segurança e a confiabilidade do sistema até o fim da rodada.

O jogo terá um sistema de pontos: se o usuário validar todos os casos da maneira certa, recebe uma quantidade de pontos.

No final de cada partida vai aparecer uma tela:

* Se ele validou da maneira correta, aparecerá: "Você protegeu o sistema e validou da maneira correta".

* Se validou usuários com erros nas fichas, aparecerá: "Você protegeu o sistema, porém não validou da forma correta".

* Se deixou um hacker invadir o sistema, aparecerá: "VOCÊ DEIXOU O SISTEMA SER INVADIDO".


## Objetivo do jogador

O jogador trabalha como uma IA, validando sistemas de fichas de identidade, o seu objetivo é validar fichas corretas, invalidar fichas com dados errados e bloquear hackers que tentarem invadir o sistema.

## Regras do jogo

Liste as principais regras do jogo.

- O jogador escolherar entre três opções: valido, invalido e bloqueado. 

- Cada partida receberá uma quantidade de pontos; porém, se validar usuários inválidos, ele não receberá pontos, mas a partida continua e os pontos de usuários válidos vão ser contados. Porém, se o jogador aceitar um hacker, ele perde todos os pontos da partida.

- A partida termina quando os casos acaba.

- Na tela do jogador, antes de ele entrar na partida, aparecerá uma página contendo as regras: só validar usuários com fichas corretas; invalidar usuários com a ficha errada (ou seja, quando no lugar do nome estiverem escritos números, nomes no campo errado ou palavras e nomes errados.); e bloquear usuários em que, no lugar do campo, estiver escrita uma linha de código, por exemplo: if true.

## Controles

Informe as teclas ou comandos utilizados no jogo.

- Escolher uma das opções com a seta para baixo, para cima ou utilizando o mouse, e confirmar a opção apertando Enter.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
