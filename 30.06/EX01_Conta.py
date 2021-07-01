class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f'''Você depositou {valor:.2f} na conta de {self.titular}
Seu saldo atual é: R${self.saldo:.2f}'''

    def sacar(self, valor):
        if valor > 0:
            if self.saldo < valor:
                return f'''{self.titular} tentou sacar R${valor:.2f}
{self.titular} seu saldo é insuficiente para sacar esse valor'''
            else:
                self.saldo -= valor
                return f'''{self.titular} sacou R${valor:.2f}
Seu saldo atual é: R${self.saldo:.2f}'''
        else:
            return f'{self.titular} você não pode sacar um valor negativo'

    def __str__(self):
        return f'''
        Titular: {self.titular}
        Saldo: R${self.saldo:.2f}
        '''