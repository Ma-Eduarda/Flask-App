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



class Usuario:
    def __init__(self, id, nome, cpf, data_nascimento):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


    def __repr__(self):
        return f'<Usuario (self.nome), (self.cpf), (self.data_nascimento)>'


    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "data_nascimento": self.data_nascimento
        }
    

if __name__ == "__main__":
    usuario = Usuario(1, "edi", "111222333", "2025-10-09")
    print(usuario)              
