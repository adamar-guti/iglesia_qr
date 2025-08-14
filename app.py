from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bienvenido a la plataforma de eventos de la iglesia</h1><p>Pronto más información...</p>"

if __name__ == "__main__":
    app.run(debug=True)

