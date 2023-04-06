from Cliente import Cliente
from Colecao import ColecaoClientes
# Criando uma coleção de clientes
clientes = ColecaoClientes()

# Adicionando alguns clientes
clientes.adicionar_cliente(Cliente('Fulano', '111.111.111-11', '01/01/2021'))
clientes.adicionar_cliente(Cliente('Ciclano', '222.222.222-22', '02/02/2021'))

# Listando os clientes
lista_de_clientes = clientes.listar_clientes()
for cliente in lista_de_clientes:
    print(cliente)


clienteEncontrado = clientes.buscaPorNome(input("Digite o nome da busca: "))
string = clienteEncontrado.__str__()



print(f"Cliente foi encontrado? " + string)
     
# Removendo um cliente
clientes.remover_cliente(lista_de_clientes[0])
