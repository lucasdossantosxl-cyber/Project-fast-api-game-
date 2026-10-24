# Project Fast API Game — RPG com Flask

API de estudo em Python para validar dados de guerreiros e simular uma batalha com armas, poderes e ataques críticos. Apesar do nome do repositório, a implementação utiliza **Flask**.

## Funcionalidades

- Validação do nome e da pontuação no cadastro de um guerreiro.
- Seleção de arma e poder elemental para a batalha.
- Resultado baseado na pontuação, com possibilidade de dano crítico.
- Respostas em JSON e script de exemplo para consumir a API.

O projeto não possui interface gráfica nem banco de dados. A rota de criação apenas valida os dados e retorna uma mensagem; não armazena o guerreiro. Cada batalha recebe seus próprios dados.

## Instalação e execução

Tenha Python 3 com pip e Git instalados. No Windows PowerShell:

```powershell
git clone https://github.com/lucasdossantosxl-cyber/Project-fast-api-game-.git
cd Project-fast-api-game-
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Se você já está na pasta local `project_FastApi`, comece pela criação do ambiente virtual. Os comandos utilizam diretamente o Python desse ambiente, sem precisar ativá-lo.

No Linux ou macOS, use `python3 -m venv .venv` e substitua `.\.venv\Scripts\python.exe` por `.venv/bin/python` nos comandos seguintes.

O servidor fica disponível em `http://127.0.0.1:5000`. Encerre com `Ctrl+C`. O comando inicia o modo de desenvolvimento (`debug=True`), destinado ao uso local.

## Rotas

As requisições devem enviar um objeto JSON com `Content-Type: application/json`. A aplicação não define página inicial nem documentação automática em `/docs`.

### `POST /criar-guerreiro`

Recebe `nome` e, opcionalmente, `pontos`. Retorna status **201** quando a validação passa ou **400** quando o nome está ausente/vazio ou a pontuação é negativa.

Em outro terminal PowerShell, com o servidor em execução:

```powershell
$guerreiro = @{ nome = "Veriff Lendário"; pontos = 85 } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:5000/criar-guerreiro" -Method Post -ContentType "application/json; charset=utf-8" -Body $guerreiro
```

Exemplo de resposta:

```json
{
  "status": "sucesso",
  "mensagem": "Guerreiro Veriff Lendário pronto para a batalha!"
}
```

### `POST /batalha`

```powershell
$batalha = @{
    nome = "Veriff"
    pontos = 85
    escolha_arma = 1
    escolha_poder = 1
} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:5000/batalha" -Method Post -ContentType "application/json" -Body $batalha
```

| Campo | Uso |
| --- | --- |
| `nome` | Nome do jogador; quando omitido, usa `Guerreiro`. |
| `pontos` | Pontuação convertida para inteiro; envie um número inteiro. |
| `escolha_arma` | Código da arma, como número ou texto. |
| `escolha_poder` | Código do poder, como número ou texto. |

| Código | Arma | Dano base | Poder | Dano bônus |
| --- | --- | --- | --- | --- |
| 1 | Espada | 30 | Fogo | 20 |
| 2 | Escudo | 15 | Agua | 10 |
| 3 | Martelo | 50 | Trovao | 25 |

Escolhas ausentes ou desconhecidas usam Martelo e Trovao como padrão. O dano soma os valores da arma e do poder. Com **50 pontos ou mais**, o jogador vence e tem **30% de chance** de dobrar o dano: o sorteio de 1 a 10 precisa resultar em 8, 9 ou 10. Abaixo de 50 pontos, o resultado é `GAME OVER`.

Exemplo de resposta sem crítico:

```json
{
  "jogador": "Veriff",
  "pontos_validados": 85,
  "arma_equipada": "Espada",
  "poder_equipado": "Fogo",
  "resultado_batalha": "VITÓRIA! Veriff venceu causando 50 de dano elemental!"
}
```

Não é necessário chamar `/criar-guerreiro` antes de `/batalha`.

## Script de exemplo

Com o servidor ligado, execute em outro terminal:

```powershell
.\.venv\Scripts\python.exe teste.py
```

O script usa `requests` para enviar um guerreiro à rota de criação e imprimir o status e a resposta. Trata-se de um exemplo de consumo, sem asserções de testes automatizados.

## Organização

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Inicia o servidor local. |
| `server.py` | Cria a aplicação Flask e registra os blueprints. |
| `routes.py` | Define a rota de criação de guerreiro. |
| `jogo.py` | Define a batalha, armas, poderes e crítico. |
| `validators.py` | Valida nome e pontuação do guerreiro. |
| `pontuacao.py` | Converte a pontuação para inteiro. |
| `teste.py` | Demonstra uma requisição HTTP com requests. |
| `requirements.txt` | Lista as dependências externas. |

## Limitações atuais

As validações são básicas: envie `nome` como texto e `pontos` como inteiro. Em `/batalha`, pontuação ausente ou nula pode causar erro interno; texto não conversível para inteiro vira zero. Outros formatos inesperados de JSON também podem causar erros. Não há autenticação, persistência ou controle de sessões de jogadores.

## Conceitos praticados

Rotas HTTP, métodos POST, respostas JSON, códigos de status, blueprints do Flask, separação em módulos, validação de entradas, consumo de API com requests e sorteios com a biblioteca padrão `random`.
