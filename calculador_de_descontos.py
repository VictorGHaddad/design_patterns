from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(Desconto_por_mais_de_quinhentos_reais(
            Sem_desconto()
        )
        ).calcula(orcamento)

        return desconto

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    orcamento.aplica_desconto_extra() 
    print(orcamento.valor) # imprime 522.5 porque descontou 5% de 550.0
    orcamento.aprova()

    orcamento.aplica_desconto_extra() 
    print(orcamento.valor) # imprime 512.05 porque descontou 2% de 522.5
    orcamento.finaliza()

    orcamento.aplica_desconto_extra() # lança exceção, porque não pode aplica desconto em um orçamento finalizado