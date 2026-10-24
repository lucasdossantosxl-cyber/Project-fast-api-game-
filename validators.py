def validar_dados_guerreiro(dados):
    if "nome" not in dados or dados["nome"] == "":
        return False, "Erro: O guerreiro precisa de um nome válido!"
    
    if "pontos" in dados and dados["pontos"] < 0:
        return False, "Erro: A pontuação não pode ser negativa!"
        
    return True, "Dados validados com sucesso!"