import json
from models.Usuario import Usuario

def get_usuarios():
    usuarios = []

    with open('data/usuarios.json', 'r', encoding='utf-8') as file:
        dados = json.load(file)

        for usuario_dados in dados:
            usuario = Usuario(
                usuario_dados["id"],
                usuario_dados["nome"],
                usuario_dados["cpf"],
                usuario_dados["data_nascimento"]
            )
            usuarios.append(usuario)

    return usuarios

def salvar_usuarios(usuarios):
    dados = [usuario.to_json() for usuario in usuarios]

    with open('data/usuarios.json', 'w', encoding='utf-8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)
