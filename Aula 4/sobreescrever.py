import random

"""
def tem_saldo():
    if saldo > 0:
        return True
    else:
        return False
"""  
  
def sacar(saldo):
    
    valor = float(input("Quanto você quer sacar?\n"))
    
    if saldo >= valor:
        saldo-=valor
        return f"Saque realizado. Retire as cédulas...\nSaldo: R$ {saldo}"
    else:
        return print("Saldo insuficiente!")
    
def transferir(saldo):
    valor = float(input("Quanto você quer transferir?\n"))
    
    if saldo >= valor:
        saldo -= valor
        return f"Transferência realizada...\nSaldo: R$ {saldo}"
    else:
        return "Saldo insuficiente!"

def depositar(saldo):
    valor = float(input("Qual o valor do depósito?\n"))
    saldo+=valor
    return saldo   

saldo = random.randint(0, 10000)
print(saldo)

escolha = int(input("QUAL SERVIÇO DESEJA REALIZAR?\n1-SACAR\n2-TRANSFERIR\n3-DEPOSITAR\n"))

if escolha == 1:
    print(sacar(saldo))
elif escolha == 2:
    print(transferir(saldo))
elif escolha == 3:
    print(depositar(saldo))
