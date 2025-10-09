class Usuario:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
    def to_json(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "data_nascimento": self.data_nascimento
        }