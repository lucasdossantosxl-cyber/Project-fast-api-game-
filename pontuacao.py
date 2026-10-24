def validar_pontuacao(resposta_usuario):
    try:
        pontos = int(resposta_usuario)
        return True, pontos
    except ValueError:
        return False, 0
