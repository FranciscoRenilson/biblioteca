#!/home/urenilson/livros/venv/bin/python
import requests

# Dados do livro a ser atualizado
livro_atualizado = {
    'id': 8,
    'titulo': 'Ano Jubilar - Edição Revisada',
    'autor': 'Santo dos Santos'
}

# Título do livro que será atualizado
titulo_para_atualizar = 'ano jubilar'

# Enviar requisição PUT para atualizar o livro pelo título
response = requests.put(f'http://localhost:5000/livros/titulo/{titulo_para_atualizar}', json=livro_atualizado)

# Exibir o código de status da resposta
print(response.status_code)  # Exibe o código de status da resposta (ex: 200 OK)

# Exibir a resposta do servidor
print(response.json())  # Exibe o conteúdo da resposta JSON (livro atualizado ou mensagem de erro)

