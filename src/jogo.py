import sys
import pygame
from fichas import FICHAS
from funcoes import avaliar_escolha, obter_mensagem_final
from dados import criar_estado_inicial, salvar_recorde, carregar_recorde

pygame.init()

# CONFIGURAÇÃO DA JANELA 
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Firewall.IA")

# CARREGAR IMAGENS DE FUNDO
fundo_inicio = pygame.transform.scale(
    pygame.image.load("assets/imagens/escritorio/pag1.jpg").convert(), (LARGURA, ALTURA)
)
fundo_regras = pygame.transform.scale(
    pygame.image.load("assets/imagens/escritorio/pag2.jpg").convert(), (LARGURA, ALTURA)
)
fundo_jogo = pygame.transform.scale(
    pygame.image.load("assets/imagens/escritorio/escritorio.jpg").convert(), (LARGURA, ALTURA)
)

relogio = pygame.time.Clock()
rodando = True
tela_atual = "INICIO"  # Estados: "INICIO", "REGRAS", "JOGO", "FINAL"

# ESTADO INICIAL DA PARTIDA
estado = criar_estado_inicial()
ARQUIVO_RECORDE = "recorde.txt"
recorde = carregar_recorde(ARQUIVO_RECORDE)

# BOTÕES CLICÁVEIS   
btn_jogar = pygame.Rect(255, 372, 195, 45) # Botão jogar
btn_iniciar = pygame.Rect(255, 375, 195, 45) # Botão iniciar
btn_valido = pygame.Rect(125, 380, 215, 35)  # Botão verde VÁLIDO
btn_invalido = pygame.Rect(130, 430, 215, 35) # Botão amarelo INVÁLIDO
btn_bloqueado = pygame.Rect(140, 480, 215, 35) # Botão vermelho BLOQUEADO
btn_reiniciar = pygame.Rect(280, 400, 240, 45) # Botão na tela final

# Fontes
fonte_titulo = pygame.font.SysFont("Arial", 22, bold=True)
fonte_texto = pygame.font.SysFont("Arial", 18, bold=True)
fonte_botao = pygame.font.SysFont("Arial", 20, bold=True)


def carregar_foto_ficha(ficha):
    """Carrega a imagem do personagem da ficha atual."""
    caminho = ficha.get("imagem", "")
    if caminho:
        try:
            img = pygame.image.load(caminho).convert_alpha()
            return pygame.transform.scale(img, (80, 80))
        except FileNotFoundError:
            return None
    return None


def desenhar_texto_quebrado(superficie, texto, fonte, cor, x, y, largura_maxima):
    """Quebra o texto em duas linhas caso o nome seja muito comprido para a prancheta."""
    palavras = texto.split(" ")
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste = f"{linha_atual} {palavra}".strip()
        if fonte.size(teste)[0] <= largura_maxima:
            linha_atual = teste
        else:
            linhas.append(linha_atual)
            linha_atual = palavra
    if linha_atual:
        linhas.append(linha_atual)

    for i, linha in enumerate(linhas):
        render = fonte.render(linha, True, cor)
        superficie.blit(render, (x, y + i * 22))

    return len(linhas)


foto_atual = carregar_foto_ficha(FICHAS[0])

while rodando:
    # 1. APENAS EVENTOS E CLIQUES AQUI DENTRO
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if tela_atual == "INICIO":
                if btn_jogar.collidepoint(evento.pos):
                    tela_atual = "REGRAS"

            elif tela_atual == "REGRAS":
                if btn_iniciar.collidepoint(evento.pos):
                    tela_atual = "JOGO"

            elif tela_atual == "JOGO":
                escolha = None
                if btn_valido.collidepoint(evento.pos):
                    escolha = "valido"
                elif btn_invalido.collidepoint(evento.pos):
                    escolha = "invalido"
                elif btn_bloqueado.collidepoint(evento.pos):
                    escolha = "bloqueado"

                if escolha is not None:
                    ficha_atual = FICHAS[estado["indice_ficha"]]
                    (
                        estado["pontos"],
                        estado["houve_invasao"],
                        estado["houve_erro"],
                    ) = avaliar_escolha(
                        ficha_atual,
                        escolha,
                        estado["pontos"],
                        estado["houve_invasao"],
                        estado["houve_erro"],
                    )

                    estado["indice_ficha"] += 1
                    if estado["indice_ficha"] < len(FICHAS):
                        foto_atual = carregar_foto_ficha(FICHAS[estado["indice_ficha"]])
                    else:
                        if estado["pontos"] > recorde:
                            recorde = estado["pontos"]
                            salvar_recorde(ARQUIVO_RECORDE, recorde)
                        tela_atual = "FINAL"

            elif tela_atual == "FINAL":
                if btn_reiniciar.collidepoint(evento.pos):
                    estado = criar_estado_inicial()
                    foto_atual = carregar_foto_ficha(FICHAS[0])
                    tela_atual = "INICIO"

    # Telas
    if tela_atual == "INICIO":
        tela.blit(fundo_inicio, (0, 0))
        txt_jogar = fonte_botao.render("JOGAR", True, (0, 0, 0))
        tela.blit(txt_jogar, txt_jogar.get_rect(center=btn_jogar.center))

    elif tela_atual == "REGRAS":
        tela.blit(fundo_regras, (0, 0))
        txt_iniciar = fonte_botao.render("INICIAR", True, (0, 0, 0))
        tela.blit(txt_iniciar, txt_iniciar.get_rect(center=btn_iniciar.center))

    elif tela_atual == "JOGO":
        tela.blit(fundo_jogo, (0, 0))
        ficha_atual = FICHAS[estado["indice_ficha"]]

        # Textos em cima dos botões já desenhados na imagem
        txt_valido = fonte_botao.render("VÁLIDO", True, (0, 0, 0))
        tela.blit(txt_valido, txt_valido.get_rect(center=btn_valido.center))

        txt_invalido = fonte_botao.render("INVÁLIDO", True, (0, 0, 0))
        tela.blit(txt_invalido, txt_invalido.get_rect(center=btn_invalido.center))

        txt_bloqueado = fonte_botao.render("BLOQUEADO", True, (0, 0, 0))
        tela.blit(txt_bloqueado, txt_bloqueado.get_rect(center=btn_bloqueado.center))

        # Título e foto na prancheta
        txt_cabecalho = fonte_titulo.render("Ficha de Cadastro", True, (0, 0, 0))
        tela.blit(txt_cabecalho, (275, 78))

        if foto_atual:
            tela.blit(foto_atual, (275, 110))

        # Dados do usuário
        linhas_nome = desenhar_texto_quebrado(
            tela, f"NOME: {ficha_atual['nome']}", fonte_texto, (0, 0, 0), 275, 200, 260
        )
        deslocamento_y = 200 + (linhas_nome * 24) + 5

        txt_idade = fonte_texto.render(f"IDADE: {ficha_atual['idade']}", True, (0, 0, 0))
        txt_cep = fonte_texto.render(f"CEP: {ficha_atual['cep']}", True, (0, 0, 0))

        tela.blit(txt_idade, (275, deslocamento_y))
        tela.blit(txt_cep, (275, deslocamento_y + 28))

        # Placar e progresso no canto superior esquerdo
        txt_pontos = fonte_texto.render(f"Pontos: {estado['pontos']}", True, (255, 255, 255))
        txt_progresso = fonte_texto.render(
            f"Ficha: {estado['indice_ficha'] + 1}/{len(FICHAS)}", True, (255, 255, 255)
        )
        tela.blit(txt_pontos, (20, 20))
        tela.blit(txt_progresso, (20, 45))

    elif tela_atual == "FINAL":
        tela.fill((25, 30, 45))
        mensagem = obter_mensagem_final(estado["houve_invasao"], estado["houve_erro"])

        txt_fim = fonte_titulo.render(mensagem, True, (255, 255, 255))
        txt_placar = fonte_texto.render(
            f"Pontuação final: {estado['pontos']}  |  Recorde: {recorde}",
            True,
            (200, 220, 255),
        )

        tela.blit(txt_fim, txt_fim.get_rect(center=(LARGURA // 2, 240)))
        tela.blit(txt_placar, txt_placar.get_rect(center=(LARGURA // 2, 300)))

        pygame.draw.rect(tela, (80, 180, 90), btn_reiniciar, border_radius=8)
        txt_reiniciar = fonte_botao.render("JOGAR NOVAMENTE", True, (0, 0, 0))
        tela.blit(txt_reiniciar, txt_reiniciar.get_rect(center=btn_reiniciar.center))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()