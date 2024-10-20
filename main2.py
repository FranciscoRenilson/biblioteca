#!/home/urenilson/livros/venv/bin/python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Carregar os dados do arquivo JSON
try:
    with open('livros.json', 'r', encoding='utf-8') as f:  # Especifica o encoding UTF-8
        livros = json.load(f)
except FileNotFoundError:
    livros = []  # Inicializa como lista vazia caso o arquivo não exista


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros=livros), 200  # jsonify já lida com ensure_ascii=False


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro=livro), 200
    return jsonify(mensagem='Livro não encontrado'), 404


@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    # Salva os dados atualizados no arquivo JSON
    with open('livros.json', 'w', encoding='utf-8') as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)

    return jsonify(novo_livro=novo_livro), 201


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice] = livro_alterado

            # Salva os dados atualizados no arquivo JSON
            with open('livros.json', 'w', encoding='utf-8') as f:
                json.dump(livros, f, indent=4, ensure_ascii=False)

            return jsonify(livro_alterado=livro_alterado), 200
    return jsonify(mensagem='Livro não encontrado'), 404


# Rota para editar livro pelo título
@app.route('/livros/titulo/<string:titulo>', methods=['PUT'])
def editar_livro_por_titulo(titulo):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('título').lower() == titulo.lower():  # Ignora maiúsculas e minúsculas
            livros[indice] = livro_alterado

            # Salva os dados atualizados no arquivo JSON
            with open('livros.json', 'w', encoding='utf-8') as f:
                json.dump(livros, f, indent=4, ensure_ascii=False)

            return jsonify(livro_alterado=livro_alterado), 200
    return jsonify(mensagem='Livro não encontrado'), 404


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

            # Salva os dados atualizados no arquivo JSON
            with open('livros.json', 'w', encoding='utf-8') as f:
                json.dump(livros, f, indent=4, ensure_ascii=False)

            return '', 204
    return jsonify(mensagem='Livro não encontrado'), 404


if __name__ == '__main__':
    app.run(debug=True)
