class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco


class Pedido:
    def __init__(
        self,
        cliente,
        itens_consumidos,
        forma_de_pagar,
        desconto,
        taxa_de_servico
    ):
        self.cliente = cliente
        self.itens_consumidos = itens_consumidos  # array de itens
        self.forma_de_pagar = forma_de_pagar
        self.desconto = desconto
        self.taxa_de_servico = taxa_de_servico

    def calcular_total(self):
        total = 0
        for item in self.itens_consumidos:  # acessando o array com itens
            total += item.preco

        return (total * (1 - self.desconto)) * (1 + self.taxa_de_servico)

    # def calcular_total_com_desconto(self):
    #     return self.calcular_total() * (1 - self.desconto)

    # def incluir_taxa_de_servico_no_total(self):
    #     total_com_desconto = self.calcular_total_com_desconto()
    #     return total_com_desconto * (1 + self.taxa_de_servico)


# Para testar!
sanduba = Item('X-tudo', 16.9)
guarana = Item('Guarana', 5.9)
fritas = Item('Fritas crocantes', 10.9)

pedido_mesa_1 = Pedido(
    'Cristiano',
    [sanduba, guarana, fritas],
    'Cartao',
    0, 0.1
)

print(pedido_mesa_1.calcular_total())
