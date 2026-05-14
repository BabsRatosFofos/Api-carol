from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

@app.route("/")
def inicio():
    return send_from_directory(app.root_path, "index.html")

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    resposta = requests.get("https://api-usuarios-i4ye.onrender.com/usuarios")
    return jsonify(resposta.json())

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(app.root_path, filename)

if __name__ == '_main_':
    app.run(debug=True)