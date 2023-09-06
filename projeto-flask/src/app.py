from flask import Flask
from os import environ
from controllers.jokes_controller import jokes_controller
from controllers.musics_controller import musics_controller
from waitress import serve

app = Flask(__name__)
# app.register_blueprint => Permite conectar os modulos da aplicação
app.register_blueprint(jokes_controller, url_prefix="/jokes")
app.register_blueprint(musics_controller, url_prefix="/musics")


def start_server(host: str = "0.0.0.0", port: int = 8000):
    if environ.get("FLASK_ENV") == "dev":
        # Servidor de desenvolvimento do Kit Werkzeug
        return app.run(debug=True, host=host, port=port)
    else:
        # Este é o waitress, otimizado para produção
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
