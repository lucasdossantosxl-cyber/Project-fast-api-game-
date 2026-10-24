from flask import Blueprint, request, jsonify
from validators import validar_dados_guerreiro

guerreiro_blueprint = Blueprint("guerreiro", __name__)

@guerreiro_blueprint.route("/criar-guerreiro", methods=["POST"])
def criar_guerreiro():
    dados_recebidos = request.json
    sucesso, mensagem = validar_dados_guerreiro(dados_recebidos)
    
    if not sucesso:
        return jsonify({"status": "erro", "mensagem": mensagem}), 400
        
    return jsonify({
        "status": "sucesso", 
        "mensagem": f"Guerreiro {dados_recebidos['nome']} pronto para a batalha!"
    }), 201