class Cliente:
    nome: str
    cpf: str
    data_de_criacao: str
    
    def __init__(self, nome: str, cpf: str, data_de_criacao: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.data_de_criacao = data_de_criacao
       
    
    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, nome: str) -> None:
        self.nome = nome
    
    def get_cpf(self) -> str:
        return self.cpf
    
    def set_cpf(self, cpf: str) -> None:
        self.cpf = cpf
    
    def get_data_de_criacao(self) -> str:
        return self.data_de_criacao
    
    def set_data_de_criacao(self, data_de_criacao: str) -> None:
        self.data_de_criacao = data_de_criacao
    
    def __str__(self) -> str:
        return f"Cliente(nome={self.nome}, cpf={self.cpf}, data_de_criacao={self.data_de_criacao})"
