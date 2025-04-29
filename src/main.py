from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY="trocar-por-chave-segura")
    @app.route("/")
    def home():
        return "Receitas Sem Fogo - Portal Online"
    return app
