class ContaBancaria:
    titulares = []
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.titulares.append(self)

    def __str__(self):
        return f'{self._titular} | {self._saldo}'
    
    @classmethod
    def listar_titulares(cls):
        print(f'{'Titular'.ljust(30)} | {'Saldo'.ljust(30)} | {'Status'}')
        for titular in cls.titulares:
            print(f'{titular._titular.ljust(30)} | {titular._saldo.ljust(30)} | {titular.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'

    def ativar_conta(self):
        self._ativo = not self._ativo
    
besta = ContaBancaria("Juninho","R$0,01")
tigrinho = ContaBancaria("Tigrinho","R$143.658.103,52")
tigrinho.ativar_conta()

ContaBancaria.listar_titulares()