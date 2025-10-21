from flask import Flask, request, jsonify
from models.InstituicaoEnsino import InstituicaoEnsino
from models.Usuario import Usuario
from Helpers.instituicoesEnsino import get_instituicoes_ensino


app = Flask(__name__)

usuarios = [Usuario(2,"João", "123.456.789-00", "2000-01-01")]

instituicoesEnsino = get_instituicoes_ensino()

@app.get("/")
def index():
    return '{"versao":"2.0.0"}', 200


## --- Rotas para Usuários ---

@app.get("/usuarios")
def getUsuarios():
    return jsonify([usuario.to_json() for usuario in usuarios]), 200


@app.get("/usuarios/<int:id>")
def getUsuariosById(id: int):
    for usuario in usuarios:
        if usuario.id == id:
            return jsonify(usuario.to_json()), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404


@app.post("/usuarios")
def setUsuarios():
    data = request.get_json()

    usuario = Usuario(
        id=data['id'],
        nome=data['nome'],
        cpf=data['cpf'],
        data_nascimento=data['data_nascimento']
    )
    usuarios.append(usuario)

    return usuario.to_json(), 201


@app.put("/usuarios/<int:id>")
def atualizarUsuario(id: int):
    for usuario in usuarios:
        if usuario.id == id:
            data = request.get_json()
            usuario.nome = data['nome']
            usuario.cpf = data['cpf']
            usuario.data_nascimento = data['data_nascimento']
            return usuario.to_json(), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404


@app.delete("/usuarios/<int:id>")
def deletarUsuario(id: int):
    for usuario in usuarios:
        if usuario.id == id:
            usuarios.remove(usuario)
            return '', 204
    return jsonify({"erro": "Usuário não encontrado"}), 404


## --- Rotas para Instituição de Ensino --- 

@app.get("/instituicoesensino")
def getInstituicoesEnsino():
    return jsonify([ie.to_json() for ie in instituicoesEnsino]), 200


@app.get("/instituicoesensino/<codigo>")
def getInstituicoesByCodigo(codigo: str):
    for ie in instituicoesEnsino:
        if ie.codigo == codigo:
            return jsonify(ie.to_json()), 200

    return 'Instituição não encontrada', 404


@app.post("/instituicoesensino")
def setInstituicoesEnsino():
    data = request.get_json()

    ie = InstituicaoEnsino(
        data["codigo"],
        data["nome"],
        data["co_uf"],
        data["co_municipio"],
        data["qt_mat_bas"],
        data["qt_mat_prof"],
        data["qt_mat_eja"],
        data["qt_mat_esp"]
    )
    instituicoesEnsino.append(ie)

    return ie.to_json(), 201


@app.put("/instituicoesensino/<codigo>")
def atualizarInstituicoesEnsino(codigo: str):
    data = request.get_json()

    for ie in instituicoesEnsino:
        if ie.codigo == codigo:
            ie.nome = data["nome"]
            ie.co_uf = data["co_uf"]
            ie.co_municipio = data["co_municipio"]
            ie.qt_mat_bas = data["qt_mat_bas"]
            ie.qt_mat_prof = data["qt_mat_prof"]
            ie.qt_mat_eja = data["qt_mat_eja"]
            ie.qt_mat_esp = data["qt_mat_esp"]
            return ie.to_json(), 200

    return 'Instituição não encontrada', 404


@app.delete("/instituicoesensino/<codigo>")
def deletarInstituicoesEnsino(codigo: str):
    for ie in instituicoesEnsino:
        if ie.codigo == codigo:
            instituicoesEnsino.remove(ie)
            return '', 204

    return 'Instituição não encontrada', 404
