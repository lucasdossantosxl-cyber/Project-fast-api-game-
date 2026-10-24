from flask import Flask
from routes import guerreiro_blueprint
from jogo import game_blueprint

app = Flask(__name__)

# Registrando ambas as rotas no mesmo servidor Flask
app.register_blueprint(guerreiro_blueprint)
app.register_blueprint(game_blueprint)