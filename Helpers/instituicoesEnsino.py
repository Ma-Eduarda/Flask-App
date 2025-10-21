import json
from models.InstituicaoEnsino import InstituicaoEnsino

def get_instituicoes_ensino():
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

    return instituicoesEnsino  