def somar (x,y):
    return x+y

def subtrair(x,y):
    return x-y

def multiplicar(x,y):
    return x*y

def dividir(x,y):
    return x/y

escolha = int(input("ESCOLHA A OPERAÇÃO:\n1-SOMAR\n2-SUBTRAIR\n3-MULTIPLICAR\n4-DIVIDIR\n"))

if escolha == 1:
    n1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
    
    n2 = float(input("DIGITE O SEGUNDO NÚMERO: "))
    
    print(f"{n1} + {n2} = {somar(n1,n2)}")
    
elif escolha == 2:
    
    n1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
    
    n2 = float(input("DIGITE O SEGUNDO NÚMERO: "))
    print(f"{n1} - {n2} = {subtrair(n1,n2)}")
    
elif escolha == 3:
    
    n1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
    
    n2 = float(input("DIGITE O SEGUNDO NÚMERO: "))
    
    print(f"{n1} x {n2} = {multiplicar(n1,n2): .2f}")
    
elif escolha == 4:
    
    n1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
    
    n2 = float(input("DIGITE O SEGUNDO NÚMERO: "))
    
    print(f"{n1} / {n2} = {dividir(n1,n2): .2f}")