import requests

url = "http://127.0.0.1:5000/criar-guerreiro"

guerreiro_valido = {
    "nome": "Veriff Lendário",
    "pontos": 85
}

print("Enviando dados para o nosso servidor...")
resposta = requests.post(url, json=guerreiro_valido)

print(f"Status do Servidor: {resposta.status_code}")
print(f"Resposta da API: {resposta.json()}")