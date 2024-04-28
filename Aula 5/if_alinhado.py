import random

def sacar(saldo):
    
    global cheque_especial
    
    valor = float(input("Quanto você quer sacar?\n"))
    
    if saldo >= valor:
        saldo-=valor
        return f"Saque realizado. Retire as cédulas...\nSaldo: R$ {saldo}"
    elif (saldo+cheque_especial)>=valor:
        opcao = int(input(f"Esse saque utilizará R$ {(saldo-valor)*-1} de seu Cheque Especial. Deseja prosseguir?\n1-SIM\n2-NÃO\n"))
        
        if opcao == 1:
            cheque_especial += saldo-valor
            saldo -= valor
            
            return f"Saque realizado. Retire as cédulas...\nSaldo: R$ {saldo}\nCheque Especial: R$ {cheque_especial}"
        elif opcao == 2:
            return print("Saque não realizado!")
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

conta_corrente = False
conta_poupanca = False

conta = int(input("QUAL O TIPO DA SUA CONTA:\n1-CORRENTE\n2-POUPANÇA\n"))

if conta == 1:
    conta_corrente = True
    if conta_corrente:
        saldo = random.randint(0, 10000)
        print(saldo)
        
        cheque_especial = 1000
        
        servico = int(input("QUAL SERVIÇO DESEJA REALIZAR?\n1-SACAR\n2-TRANSFERIR\n3-DEPOSITAR\n"))
        
        if servico == 1:
            print(sacar(saldo))
        elif servico == 2:
            print(transferir(saldo))
        elif servico == 3:
            print(depositar(saldo))
        else:
            print("OPÇÃO INVÁLIDA!")
   
elif conta == 2:
    conta_poupanca = True
    if conta_poupanca:
        saldo = random.randint(0, 10000)
        print(saldo)
        
        cheque_especial = 0
        
        servico = int(input("QUAL SERVIÇO DESEJA REALIZAR?\n1-SACAR\n2-TRANSFERIR\n3-DEPOSITAR\n"))
        
        if servico == 1:
            print(sacar(saldo))
        elif servico == 2:
            print(transferir(saldo))
        elif servico == 3:
            print(depositar(saldo))
        else:
            print("OPÇÃO INVÁLIDA!")


