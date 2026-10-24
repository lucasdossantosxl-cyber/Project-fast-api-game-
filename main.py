from server import app

if __name__ == "__main__":
    print(" Servidor do RPG Ativado!")
    print("Endpoints Prontos:")
    print("   -> POST http://127.0.0.1:5000/criar-guerreiro")
    print("   -> POST http://127.0.0.1:5000/batalha")
    app.run(debug=True)