class Pessoa:
    def __init__(self, nome, idade, comportamento=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.comportamento = comportamento
        self.comendo = comendo
    def comer(self, comida):
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return
        print(f"{self.nome} está comendo")
        self.comendo = True
    def para_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo")
            return
        print(f"{self.nome} parou de comer")
        self.comendo = False