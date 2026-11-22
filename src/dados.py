PONTOS_INICIAIS = 0
INDICE_FICHA_INICIAL = 0
HOUVE_INVASAO_INICIAL = False
HOUVE_ERRO_INICIAL = False


def criar_estado_inicial():
    return {
        "pontos": PONTOS_INICIAIS,
        "indice_ficha": INDICE_FICHA_INICIAL,
        "houve_invasao": HOUVE_INVASAO_INICIAL,
        "houve_erro": HOUVE_ERRO_INICIAL,
    }


def salvar_recorde(caminho_arquivo, pontuacao):
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0