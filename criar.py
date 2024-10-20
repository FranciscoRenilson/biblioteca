#!/home/urenilson/livros/venv/bin/python
import requests

# Criar um novo livro
novo_livro = {
    'id': 8,
    'titulo': 'ano jubilar',
    'autor': 'santo dos santos'
}
response = requests.post('http://localhost:5000/livros', json=novo_livro)
print(response.status_code)  # Exibe o código de status da resposta (ex: 201 Created)
