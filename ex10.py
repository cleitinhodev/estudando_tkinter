"""
10. Classe ContaBancaria
Crie uma classe ContaBancaria com os atributos titular e saldo.
Crie dois métodos:

depositar(valor) que adiciona ao saldo

sacar(valor) que subtrai do saldo (se houver dinheiro suficiente)
"""


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Valor R$ {valor:.2f} Depositado com Sucesso\n'
              f'Saldo Atual R$ {self.saldo:.2f}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo insuficiente!\n'
                  f'Saldo Atual R$ {self.saldo:.2f}')
        else:
            self.saldo -= valor
            print(f'Valor R$ {valor:.2f} Retirado com Sucesso\n'
                  f'Saldo Atual R$ {self.saldo:.2f}')


minha_conta = ContaBancaria('Manoel', 1200)

print('Bem vindo ao Banco das Classes!')

while True:
    print('1 - DEPOSITAR\n'
          '2 - SACAR\n'
          '3 - SAIR')
    acao = int(input('O que deseja fazer?: '))

    if acao == 1:
        dinheiro = float(input('Quanto deseja depositar?: '))
        minha_conta.depositar(dinheiro)
    elif acao == 2:
        dinheiro = float(input('Quanto deseja Sacar?: '))
        minha_conta.sacar(dinheiro)
    else:
        break

print('Sessão Encerrada, tenha um bom dia! :)')
