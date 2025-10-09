from flask import Flask, request, jsonify
from models.InstituicaoEnsino import InstituicaoEnsino
from models.Usuario import Usuario
import json

app = Flask(__name__)

usuarios = [Usuario("João", "123.456.789-00", "2000-01-01")]

##ie = InstituicaoEnsino("25000012", "EMEF JOAO ALVES",
##                       25, "2501005", 779, 0, 104, 43)
##instituicoesEnsino = [ie]

instituicoesEnsino = []
with open('data/instituicoes_paraiba.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)
    for ie_dados in dados:
        ie = InstituicaoEnsino(
            ie_dados["codigo"],
            ie_dados["nome"],
            ie_dados["co_uf"],
            ie_dados["co_municipio"],
            ie_dados["qt_mat_bas"],
            ie_dados["qt_mat_prof"],
            ie_dados["qt_mat_eja"],
            ie_dados["qt_mat_esp"]
        )
        instituicoesEnsino.append(ie)


@app.get("/")
def index():
    return '{"versao":"2.0.0"}', 200


## --- Rotas para Usuários ---

@app.get("/usuarios")
def getUsuarios():
    return jsonify([usuario.to_json() for usuario in usuarios]), 200


@app.get("/usuarios/<int:id>")
def getUsuariosById(id: int):
    if id < 0 or id >= len(usuarios):
        return 'Usuário não encontrado', 404

    return jsonify(usuarios[id].to_json())


@app.post("/usuarios")
def setUsuarios():
    data = request.get_json()

    usuario = Usuario(
        nome=data['nome'],
        cpf=data['cpf'],
        data_nascimento=data['data_nascimento']
    )
    usuarios.append(usuario)

    return usuario.to_json(), 201




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