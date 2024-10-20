#!/home/urenilson/livros/venv/bin/python
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Carregar os dados do arquivo JSON
try:
    with open('livros.json', 'r') as f:
        livros = json.load(f)
except FileNotFoundError:
    livros = []  # Inicializa como lista vazia caso o arquivo não exista


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404


@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    # Salva os dados atualizados no arquivo JSON
    with open('livros.json', 'w') as f:
        json.dump(livros, f, indent=4)

    return jsonify(novo_livro), 201


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice] = livro_alterado

            # Salva os dados atualizados no arquivo JSON
            with open('livros.json', 'w') as f:
                json.dump(livros, f, indent=4)

            return jsonify(livro_alterado)
    return jsonify({'mensagem': 'Livro não encontrado'}), 404


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

            # Salva os dados atualizados no arquivo JSON
            with open('livros.json', 'w') as f:
                json.dump(livros, f, indent=4)

            return '', 204
    return jsonify({'mensagem': 'Livro não encontrado'}), 404


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(port=5000,host='localhost',debug=True)
