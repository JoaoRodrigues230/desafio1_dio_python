class Pessoa(object):
    __nome = ""
    __idade = 0

    def __init__(self, n, i):
        self.__nome = n
        self.__idade = i
    
    def exibir(self):
        return f"{self.__nome} tem {self.__idade} anos"
    
class PF(Pessoa):
    __cpf = ""
    
    def __init__(self, n, i, cpf):
        super().__init__(n, i)
        self.__cpf = cpf

    def exibir(self):
        return super().exibir()+ " | CPF: " + self.__cpf
    
class PJ(Pessoa):
    
    __cnpj = ""
    
    def __init__(self, n, i, cnpj):
        super().__init__(n, i)
        self.__cnpj = cnpj
    
    def exibir(self):
        return super().exibir() + " | CNPJ: " + self.__cnpj
    
if __name__ == "__main__":
    
    p1 = Pessoa (input(), input())
    p2 = Pessoa("Vini", 19)
    pf = PF("João", 19, "53813187829")
    pj = PJ("Unisantos", 70, "234.1345.0001/000")
    
    pessoas = [p1, p2, pf, pj]
    
    for p in pessoas:
        print(p.exibir())
                
    