import random
import os

saldo = random.randint(0, 200)
cheque_especial = 0
extrato = ""
limite_saque = 3
valor_limite = 500

def limpar_tela():
    if os.name == 'nt':  
        os.system('cls')  
    else:
        os.system('clear')  

def sacar(saldo):
    global extrato
    global cheque_especial
    global limite_saque
    
    if limite_saque == 0:
        return "Limite de saques diários atingidos..."
    
    valor = float(input("Quanto você quer sacar?\nR$ "))
    limpar_tela()
    
    if valor>valor_limite:
        return f"Valor excede o limite de saque. Limite de Saque: R$ {valor_limite}"
    
    if saldo >= valor:
        saldo -= valor
        extrato += f"Saque ATM: R$ {valor}\n"
        limite_saque -= 1
        return f"Saque realizado. Retire as cédulas...\nSaldo: R$ {saldo}\n"
    elif (saldo + cheque_especial) >= valor:
        opcao = -1
        while opcao != 2:
            opcao = int(input(f"Esse saque utilizará R$ {(saldo - valor) * -1} de seu Cheque Especial. Deseja prosseguir?\n1-SIM\n2-NÃO\n"))
        
            if opcao == 1:
                cheque_especial += saldo - valor
                saldo -= valor
                extrato += f"Saque ATM: R$ {valor}\n"
                limite_saque -= 1
                return f"Saque realizado. Retire as cédulas...\nSaldo: R$ {saldo}\nCheque Especial: R$ {cheque_especial}\n"
        else:
            return print("Saque não realizado!\n")
    else:
        return print("Saldo insuficiente!\n")
    
def depositar(saldo):
    global extrato
    global cheque_especial
    
    while True:
        valor = float(input("Qual o valor do depósito?\n"))
        if valor>0:
            if cheque_especial<300:
                cheque_especial+=valor
                if cheque_especial>300:
                    saldo = cheque_especial-300
                    cheque_especial = 300
                    extrato+= f"Depósito: R$ {valor}\n"
                    return f"Deposíto Realizado. Saldo Atual: R$ {saldo}" 
            
            
        else:
            print("Valor informado não é válido, por favor tente novamente...")

def mostrar_extrato(saldo, cheque_especial):
    global extrato
    
    if extrato:
        print("\nExtrato:\n")
        print(extrato)
        print(f"Saldo: R$ {saldo}")
        print(f"Cheque Especial: R$ {cheque_especial}")
    else:
        print("Extrato não pode ser impresso. Nenhuma operação realizada...")

conta_corrente = False
conta_poupanca = False

conta = -1

while conta != 0:
    conta = int(input("QUAL O TIPO DA SUA CONTA:\n1-CORRENTE\n2-POUPANÇA\n0-SAIR\n"))
    
    limpar_tela()

    if conta == 1:
        conta_corrente = True
        if conta_corrente:
            print(f"Saldo: R$ {saldo}")
            cheque_especial = 300
            
            while True:
                servico = int(input("QUAL SERVIÇO DESEJA REALIZAR?\n1-SACAR\n2-DEPOSITAR\n3-EXTRATO\n0-VOLTAR\n"))
                limpar_tela()

                if servico == 1:
                    print(sacar(saldo))
                    
                elif servico == 2:
                    print(depositar(saldo))
                    
                elif servico == 3:
                    mostrar_extrato(saldo, cheque_especial)
                    
                elif servico == 0:
                    break
                
                else:
                    print("OPÇÃO INVÁLIDA!")
   
    elif conta == 2:
        conta_poupanca = True
        if conta_poupanca:
            print(f"Saldo: R$ {saldo}")
            cheque_especial = 0
            
            while True:
                servico = int(input("QUAL SERVIÇO DESEJA REALIZAR?\n1-SACAR\n2-DEPOSITAR\n3-EXTRATO\n0-VOLTAR\n"))
                limpar_tela()

                if servico == 1:
                    print(sacar(saldo))
                    
                elif servico == 2:
                    print(depositar(saldo))
                    
                elif servico == 3:
                    mostrar_extrato(saldo, cheque_especial)
                    
                elif servico == 0:
                    break
                
                else:
                    print("OPÇÃO INVÁLIDA!")

    elif conta == 0:
        print("\nOBRIGADO POR UTILIZAR O SISTEMA!")

    else:
        print("OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.")
