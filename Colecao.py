from Cliente import Cliente
from typing import List, Union

class ColecaoClientes:
    def __init__(self) -> None:
        self.clientes = []
    
    def adicionar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)
    
    def remover_cliente(self, cliente: Cliente) -> None:
        self.clientes.remove(cliente)
    
    def listar_clientes(self) -> List[Cliente]:
        return self.clientes

    def buscaPorNome(self,nome : str):
        nome : str
        cliente : Cliente
        for cliente in self.clientes:
            if cliente.get_nome().__eq__(nome):
                return cliente
        return None
