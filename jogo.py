from flask import Blueprint, request, jsonify
import random
from pontuacao import validar_pontuacao

game_blueprint = Blueprint("game", __name__)

@game_blueprint.route("/batalha", methods=["POST"])
def iniciar_batalha():
    dados = request.json
    nome_guerreiro = dados.get("nome", "Guerreiro")
    
    sucesso, pontos = validar_pontuacao(dados.get("pontos"))
    
    dados_armas = {
        '1': {"nome": "Espada", "dano_base": 30},
        '2': {"nome": "Escudo", "dano_base": 15},
        '3': {"nome": "Martelo", "dano_base": 50}
    }
    dados_poderes = {
        '1': {"nome": "Fogo", "dano_bonus": 20, "efeito": "incendiando o oponente"},
        '2': {"nome": "Agua", "dano_bonus": 10, "efeito": "criando uma barreira"},
        '3': {"nome": "Trovao", "dano_bonus": 25, "efeito": "eletrocutando tudo"}
    }
    
    arma = dados_armas.get(str(dados.get("escolha_arma")), dados_armas['3'])
    poder = dados_poderes.get(str(dados.get("escolha_poder")), dados_poderes['3'])
    
    dano_total = arma["dano_base"] + poder["dano_bonus"]
    sorteio_critico = random.randint(1, 10)
    
    if pontos >= 50:
        if sorteio_critico >= 8:
            dano_total *= 2
            resultado = f"CRÍTICO LENDÁRIO! {nome_guerreiro} causou {dano_total} de dano com {arma['nome']} de {poder['nome']}!"
        else:
            resultado = f"VITÓRIA! {nome_guerreiro} venceu causando {dano_total} de dano elemental!"
    else:
        resultado = f"GAME OVER! {nome_guerreiro}, sua jornada terminou mais cedo."
        
    return jsonify({
        "jogador": nome_guerreiro,
        "pontos_validados": pontos,
        "arma_equipada": arma["nome"],
        "poder_equipado": poder["nome"],
        "resultado_batalha": resultado
    })