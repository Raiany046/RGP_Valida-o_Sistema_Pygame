import sys
import pygame

pygame.init()

# Inicializar
tela = pygame.display.set_mode((700, 600))
pygame.display.set_caption("RPG: IA_Validação_de_sistema")

# Imagens de fundo
fundo_primeira = pygame.image.load("assets/imagens/escritorio/pag2.jpg").convert()
fundo_primeira = pygame.transform.scale(fundo_primeira, (700, 600))

fundo_segunda = pygame.image.load("assets/imagens/escritorio/pag1.jpg").convert()
fundo_segunda = pygame.transform.scale(fundo_segunda, (700, 600))

fundo_escritorio = pygame.image.load("assets/imagens/escritorio/escritorio.jpg").convert()
fundo_escritorio = pygame.transform.scale(fundo_escritorio, (700, 600))

relogio = pygame.time.Clock()
rodando = True

# Controla qual tela está ativa: "INICIO(pag1)", "REGRAS(pag2)" ou "JOGO(casos)"
tela_atual = "INICIO"

# Retângulos dos botões (ajuste as posições x, y se precisar alinhar com a sua arte)
btn_jogar = pygame.Rect(200, 375, 220, 38)
btn_continuar = pygame.Rect(200, 375, 220, 38) # Botão para sair das regras e ir pro jogo

btn_valido = pygame.Rect(100, 380, 220, 35)
btn_invalido = pygame.Rect(100, 430, 235, 35)
btn_bloqueado = pygame.Rect(100, 480, 260, 35)

fonte = pygame.font.SysFont("Arial", 24, bold=True)

while rodando:
    # 1. EVENTOS (Cliques e Teclado)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if tela_atual == "INICIO":
                if btn_jogar.collidepoint(evento.pos):
                    tela_atual = "REGRAS"

            elif tela_atual == "REGRAS":
                
                # Clique no botão ou em qualquer lugar para avançar pro jogo
                if btn_continuar.collidepoint(evento.pos):
                    tela_atual = "JOGO"
            

            elif tela_atual == "JOGO":
                if btn_valido.collidepoint(evento.pos):
                    print("VÁLIDO!")
                elif btn_invalido.collidepoint(evento.pos):
                    print("INVÁLIDO!")
                elif btn_bloqueado.collidepoint(evento.pos):
                    print("BLOQUEADO!")

        # Teclado (Enter avança das regras para o jogo)
        if evento.type == pygame.KEYDOWN:
            if tela_atual == "REGRAS" and evento.key == pygame.K_RETURN:
                tela_atual = "JOGO"

    # 2. DESENHO DAS TELAS (Separado por estado!)
    if tela_atual == "INICIO":
        tela.blit(fundo_primeira, (0, 0))
        txt_valido = fonte.render("JOGAR", True, (0, 0, 0))
        tela.blit(txt_valido, txt_valido.get_rect(center=btn_jogar.center))
        # Se a sua imagem pag2.jpg já tiver o botão desenhado, não precisa desenhar retângulo

    elif tela_atual == "REGRAS":
        tela.blit(fundo_segunda, (0, 0))
       
        txt_cont = fonte.render("INICIAR", True, (0, 0, 0))
        tela.blit(txt_cont, txt_cont.get_rect(center=btn_continuar.center))

    elif tela_atual == "JOGO":
        tela.blit(fundo_escritorio, (0, 0))

        # Renderizar e centralizar os textos dentro de cada Rect
        txt_valido = fonte.render("VÁLIDO", True, (0, 0, 0))
        tela.blit(txt_valido, txt_valido.get_rect(center=btn_valido.center))

        txt_invalido = fonte.render("INVÁLIDO", True, (0, 0, 0))
        tela.blit(txt_invalido, txt_invalido.get_rect(center=btn_invalido.center))

        txt_bloqueado = fonte.render("BLOQUEADO", True, (0, 0, 0))
        tela.blit(txt_bloqueado, txt_bloqueado.get_rect(center=btn_bloqueado.center))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()