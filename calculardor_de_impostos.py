from orcamento import Orcamento
from impostos import ISS, ICMS, IKCV, ICPP

# -*- coding: UTF-8 -*-
# calculador_de_impostos.py
# apenas exemplo, não funciona porque não temos as novas classes de impostos ainda
class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        return print(valor)

if __name__ == '__main__':

    from orcamento import Orcamento, Item
    from impostos import ISS, ICMS, ICPP, IKCV

    orcamento = Orcamento(0)
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador_de_impostos = Calculador_de_impostos()
    print('ISS e ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS()) # imprime 50.0
    calculador_de_impostos.realiza_calculo(orcamento, ICMS()) # imprime 30.0

    print ('ISS_com_ICMS')
    # veja, não é necessária mais uma classe. Imposto recebe outro em seu construtor
    ISS_com_ICMS = ISS(ICMS())
    calculador_de_impostos.realiza_calculo(orcamento, ISS_com_ICMS) # imprime 80

    print ('ICPP e IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP()) # imprime 25.0
    calculador_de_impostos.realiza_calculo(orcamento, IKCV()) # imprime 30.0
