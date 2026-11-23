PONTOS_POR_ACERTO = 10

ESCOLHA_CORRETA = {
    "valido": "valido",
    "invalido": "invalido",
    "hacker": "bloqueado",
}

ESCOLHAS_DE_INVASAO = {
    ("hacker", "valido"),
}

MENSAGENS_FINAIS = {
    "invasao": "VOCÊ DEIXOU O SISTEMA SER INVADIDO",
    "erro": "Você protegeu o sistema, porém não validou da forma correta",
    "perfeito": "Você protegeu o sistema e validou da maneira correta",
}


def avaliar_escolha(ficha, escolha_jogador, pontos_atuais, houve_invasao, houve_erro):
    tipo_real = ficha["tipo"].lower()

    if (tipo_real, escolha_jogador) in ESCOLHAS_DE_INVASAO:
        pontos_atuais = 0
        houve_invasao = True
    elif escolha_jogador == ESCOLHA_CORRETA[tipo_real]:
        pontos_atuais += PONTOS_POR_ACERTO
    else:
        houve_erro = True

    return pontos_atuais, houve_invasao, houve_erro


def obter_mensagem_final(houve_invasao, houve_erro):
    if houve_invasao:
        return MENSAGENS_FINAIS["invasao"]
    if houve_erro:
        return MENSAGENS_FINAIS["erro"]
    return MENSAGENS_FINAIS["perfeito"]


def calcular_pontos(pontos_atual, pontos_ganhos):
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    return vida_atual - dano


def jogador_perdeu(vidas):
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    return retangulo_1.colliderect(retangulo_2)