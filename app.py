from flask import Flask, request, jsonify

app = Flask(__name__)

livros = []

@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def buscar_livro(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return {"erro": "Livro não encontrado"}, 404

@app.route('/livros', methods=['POST'])
def criar_livro():
    dados = request.json

    if not dados:
        return {"erro": "JSON vazio"}, 400

    if not dados.get('título') or not dados.get('autor'):
        return {"erro": "Título e autor são obrigatórios"}, 400

    if dados.get('ano', 0) < 0:
        return {"erro": "Ano inválido"}, 400

    for l in livros:
        if l['titulo'] == dados['titulo']:
            return {"erro": "Livro já cadastrado"}, 400

    novo_livro = {
        "id": len(livros) + 1,
        "título": dados['titulo'],
        "autorP": dados['autor'],
        "ano": dados['ano']
    }

    livros.append(novo_livro)

    return {
        "mensagem": "Livro cadastrado com sucesso",
        "livro": novo_livro
    }, 201

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    dados = request.json

    for livro in livros:
        if livro['id'] == id:
            livro['titulo'] = dados.get('titulo', livro['titulo'])
            livro['autor'] = dados.get('autor', livro['autor'])
            livro['ano'] = dados.get('ano', livro['ano'])

            return {"mensagem": "Livro atualizado com sucesso", "livro": livro}

    return {"erro": "Livro não encontrado"}, 404

@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return {"mensagem": "Livro removido com sucesso"}

    return {"erro": "Livro não encontrado"}, 404

if __name__ == '__main__':
    app.run(debug=True)